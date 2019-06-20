#
from django.db import models
from mywing.angel.models import Angel


class News(models.Model):
    author = models.CharField(max_length=32)
    published_at = models.DateTimeField(auto_now=True)
    title = models.TextField()
    content = models.TextField()


class Board(models.Model):
    description = models.CharField(max_length=256)


class BoardSnapshot(models.Model):
    captured_at = models.DateTimeField(auto_now=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='snapshots')

    class Meta:
        ordering = ['-captured_at']


class BoardSnapshotItem(models.Model):
    snapshot = models.ForeignKey(BoardSnapshot, related_name='items', on_delete=models.CASCADE)
    order = models.IntegerField()
    angel = models.ForeignKey(Angel, null=True, on_delete=models.SET_NULL)
    value = models.CharField(max_length=16)
