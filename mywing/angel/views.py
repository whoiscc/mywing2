#
from rest_framework import generics, mixins, serializers
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from cas import CASClient
from django.contrib.auth.models import User
from urllib.parse import unquote
from mywing.angel.serializers import AngelSerializer, CASLoginSerializer
from mywing.angel.models import Angel


class RetrieveAngelView(generics.RetrieveAPIView):
    queryset = Angel.objects.all()
    serializer_class = AngelSerializer


@api_view(['GET'])
def retrieve_self_view(request):
    return Response(AngelSerializer(request.user.angel).data)


class CASLoginView(generics.GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = CASLoginSerializer
    queryset = Angel.objects.all()

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        if data['domain'] == 'xjtu':
            cas_client = CASClient(
                version='CAS_2_SAML_1_0',
                server_url='https://cas.xjtu.edu.cn',
                service_url=data['service']
            )
            netid, attr, _ = cas_client.verify_ticket(data['ticket'])
            if netid is None:
                raise serializers.ValidationError('fail to verify ticket (xjtu)')
            identifier = 'xjtu-' + netid
            try:
                user = User.objects.get(username=identifier)
                angel = user.angel
            except User.DoesNotExist:
                user = User.objects.create_user(username=identifier)
                user.set_unusable_password()
                user.save()
                angel = Angel(user=user, real_name=unquote(attr['cn']))
                angel.save()
        else:
            raise serializers.ValidationError('unknown domain')
        token = Token.objects.create(user=user)
        return Response({**AngelSerializer(angel).data, 'token': token.key})


@api_view(['POST'])
def logout(request):
    request.user.token.delete()
    return Response('ok')
