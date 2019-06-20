#

from rest_framework import serializers
from mywing.task.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'description', 'cost', 'owner', 'helper', 'status', 'contribution')
        read_only_fields = ('status', 'owner', 'helper', 'contribution')
