from django.db import models


class CommunityPerson(models.Model):
    ROLE_CHOICES = (
        ('leader', 'ผู้นำชุมชน'),
        ('wise_man', 'ปราชญ์ชุมชน'),
    )

    name = models.CharField(null=False, blank=False, max_length=150)
    role = models.CharField(
        null=False,
        blank=False,
        choices=ROLE_CHOICES,
        default='pending',
        max_length=10
    )
    community = models.ForeignKey(
        'communities.Community',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.name} ({self.role})'
