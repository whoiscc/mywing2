#

from rest_framework import serializers
from mywing.angel.models import Angel
from mywing.task.serializers import TaskSerializer


class AngelSerializer(serializers.ModelSerializer):
    owned_tasks = TaskSerializer(many=True, read_only=True)
    helped_tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = Angel
        fields = ('id', 'real_name', 'contribution', 'owned_tasks', 'helped_tasks')
        read_only_fields = ('id', 'real_name', 'contribution')


class CASLoginSerializer(serializers.Serializer):
    domain = serializers.CharField()
    service = serializers.CharField()
    ticket = serializers.CharField()
