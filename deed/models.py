from django.db import models
from django.contrib.auth import get_user_model


class Deed(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    talent = models.ForeignKey('talent.Talent', on_delete=models.CASCADE)
    points = models.PositiveIntegerField()
    description = models.TextField(blank=True, null=True)
    times_completed = models.PositiveIntegerField(default=1)
