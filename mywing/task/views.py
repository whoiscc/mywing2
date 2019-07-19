#

from rest_framework import generics, serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.utils import timezone
from mywing.task.models import Task
from mywing.task.serializers import TaskSerializer


class RecentUnacceptedTasksView(generics.ListAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(status=Task.CREATED).exclude(owner=self.request.user.angel).order_by('-cost')[:20]


class UpdateTaskView(generics.UpdateAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user.angel)


class CreateTaskView(generics.CreateAPIView):
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user.angel)


@api_view(['POST'])
def accept(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.user.angel == task.owner:
        raise serializers.ValidationError('cannot accept owned task')
    if task.status != Task.CREATED:
        raise serializers.ValidationError('invalid task status')
    task.status = Task.ACCEPTED
    task.helper = request.user.angel
    task.accepted_at = timezone.now()
    task.save()
    return Response(TaskSerializer(task).data)


@api_view(['POST'])
def finish(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.user.angel != task.helper:
        raise serializers.ValidationError('cannot finish not-helped task')
    if task.status != Task.ACCEPTED:
        raise serializers.ValidationError('invalid task status')
    task.status = Task.FINISHED
    try:
        contribution = request.data['contribution']
        assert 0 <= contribution <= task.cost
        task.contribution = contribution
    except:
        raise serializers.ValidationError('invalid contribution')
    task.finished_at = timezone.now()
    task.save()
    return Response(TaskSerializer(task).data)


@api_view(['POST'])
def complete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.user.angel != task.owner:
        raise serializers.ValidationError('cannot complete not-owned task')
    if task.status != Task.FINISHED:
        raise serializers.ValidationError('invalid task status')
    task.status = Task.COMPLETED
    task.save()
    task.helper.contribution += task.contribution
    task.completed_at = timezone.now()
    task.helper.save()
    return Response(TaskSerializer(task).data)


@api_view(['POST'])
def cancel(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.user.angel not in [task.owner, task.helper]:
        raise serializers.ValidationError('cannot cancel not-owned or -helped task')
    if task.status not in [Task.CREATED, Task.ACCEPTED, Task.FINISHED]:
        raise serializers.ValidationError('invalid task status')
    task.status = Task.CANCELED
    task.canceled_at = timezone.now()
    task.save()
    return Response(TaskSerializer(task).data)
