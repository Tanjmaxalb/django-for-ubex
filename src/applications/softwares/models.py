from django.db import models

from applications.core.models import TimestampedModel
from applications.vulnerabilities.models import Vulnerability


class Software(TimestampedModel):
    name = models.CharField(db_index=True, max_length=255)
    description = models.TextField()
    vulnerability = models.ForeignKey(
        Vulnerability, on_delete=models.CASCADE, null=True)
