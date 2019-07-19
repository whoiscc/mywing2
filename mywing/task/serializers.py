#

from rest_framework import serializers
from mywing.task.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'description', 'cost', 'owner', 'helper', 'status', 'contribution', 'created_at', 'accepted_at', 'finished_at', 'completed_at', 'canceled_at')
        read_only_fields = ('status', 'owner', 'helper', 'contribution', 'created_at', 'accepted_at', 'finished_at', 'completed_at', 'canceled_at')
