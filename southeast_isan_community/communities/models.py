from django.db import models


class Community(models.Model):
    name = models.CharField(null=False, blank=False, max_length=150)