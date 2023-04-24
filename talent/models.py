from django.db import models
from django.contrib.auth import get_user_model


class Talent(models.Model):
    title = models.CharField(max_length=256)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
