import datetime

from django.db import models
from django.contrib.postgres.fields import JSONField, ArrayField

# Create your models here. Class is a subclass of django.db.models.Model
class citations(models.Model):
    def __str__(self):
        return self.title

    id = models.CharField(primary_key=True, max_length=1000) 
    chapter_number = models.IntegerField()
    title = models.CharField(max_length=1000)
    proofs = JSONField()
    paragraphs = ArrayField(models.TextField())

    def get_all_data(self):
        return {
            'title': self.title,
            'paragraphs': self.paragraphs,
            'proofs': self.proofs,
            'chapter_number': self.chapter_number
        }