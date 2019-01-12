from django.db import models


class Community(models.Model):
    name = models.CharField(null=False, blank=False, max_length=150)
    regional_dialect = models.CharField(
        null=True,
        blank=True,
        max_length=150
    )
    faith = models.CharField(null=True, blank=True, max_length=150)
    folk_game = models.CharField(null=True, blank=True, max_length=150)

    class Meta:
        verbose_name_plural = 'communities'

    def __str__(self):
        return self.name
