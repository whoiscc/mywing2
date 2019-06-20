#
from django.conf import settings
from django.db import models


class Angel(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    real_name = models.CharField(max_length=32)
    contribution = models.FloatField(default=0.0)

    def __str__(self):
        return f'Angel#{self.id}: {self.real_name}'
