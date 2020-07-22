from django.db import models

from applications.core.models import TimestampedModel


class Vulnerability(TimestampedModel):
    name = models.CharField(db_index=True, max_length=255)
    description = models.TextField()
