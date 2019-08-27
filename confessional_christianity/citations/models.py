import datetime

from django.db import models
from django.contrib.postgres.fields import JSONField, ArrayField

from confessions.models import Confessions, Headings, Passages

# Create your models here. Class is a subclass of django.db.models.Model
class Citations(models.Model):
    def __str__(self):
        return str(self.id)

    id = models.CharField(primary_key=True, max_length=1000)
    confession = models.ForeignKey(Confessions, on_delete=models.CASCADE)
    heading = models.ForeignKey(Headings, on_delete=models.CASCADE)
    passage = models.ForeignKey(Passages, on_delete=models.CASCADE)
    referenceIdentifier = JSONField()
    scripture = ArrayField(models.TextField())
    tags = ArrayField(models.TextField())

    def get_detail(self):
        return {
            'scripture': self.scripture,
            'citationId': self.id,
            'heading': self.heading.title,
        }
