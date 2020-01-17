"""Create a model for the jobs."""
from django.db import models
from django.utils import timezone


class Job(models.Model):
    """Create fields for jobs."""

    url = models.CharField(max_length=250, unique=True)
    title = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        """Human readable format for the title."""
        return self.title

    class Meta:
        """Order with title."""

        ordering = ['title']
