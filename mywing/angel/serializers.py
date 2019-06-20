#

from rest_framework import serializers
from mywing.angel.models import Angel


class AngelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Angel
        fields = ('id', 'real_name', 'contribution', 'owned_tasks', 'helped_tasks')
        read_only_fields = ('id', 'real_name', 'contribution')


class CASLoginSerializer(serializers.Serializer):
    domain = serializers.CharField()
    service = serializers.CharField()
    ticket = serializers.CharField()
