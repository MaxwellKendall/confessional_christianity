import datetime

from django.db import models
from django.contrib.postgres.fields import JSONField, ArrayField

# Create your models here. Class is a subclass of django.db.models.Model
class wcf(models.Model):
    def __str__(self):
        return self.title
    id = models.CharField(primary_key=True, max_length=1000) 
    chapter_number = models.IntegerField()
    title = models.CharField(max_length=1000)
    # map: proof_reference_from_paragraph: proof
    proofs = JSONField()
    # array
    paragraphs = ArrayField(models.TextField())

    def get_details(self):
        # Do something here in the future?
        return self.title + self.chapter_number
