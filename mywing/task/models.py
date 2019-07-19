from django.db import models
from django.utils import timezone

from mywing.angel.models import Angel


class Task(models.Model):
    description = models.CharField(max_length=256)
    cost = models.FloatField()
    owner = models.ForeignKey(Angel, on_delete=models.SET_NULL, null=True, related_name='owned_tasks')
    helper = models.ForeignKey(Angel, on_delete=models.SET_NULL, null=True, related_name='helped_tasks')
    contribution = models.FloatField(default=0.0)

    created_at = models.DateTimeField(blank=True, null=True, default=timezone.now())
    accepted_at = models.DateTimeField(blank=True, null=True)
    finished_at = models.DateTimeField(blank=True, null=True)
    completed_at = models.DateTimeField(blank=True, null=True)
    canceled_at = models.DateTimeField(blank=True, null=True)

    CREATED = 0
    ACCEPTED = 1
    FINISHED = 2
    COMPLETED = 3
    INVALID = -1
    CANCELED = -2
    STATUS_CHOICES = [
        (CREATED, 'created'),
        (ACCEPTED, 'accepted'),
        (FINISHED, 'finished'),
        (COMPLETED, 'completed'),
        (INVALID, 'invalid'),
        (CANCELED, 'canceled'),
    ]
    status = models.IntegerField(choices=STATUS_CHOICES, default=CREATED)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return f'Task#{self.id}: {self.description}'
