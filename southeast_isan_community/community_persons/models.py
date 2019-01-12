from django.db import models


class CommunityPerson(models.Model):
    name = models.CharField(null=False, blank=False, max_length=150)
    community = models.ForeignKey(
        'communities.Community',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name
