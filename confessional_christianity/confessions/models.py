import datetime

from django.db import models
from django.contrib.postgres.fields import JSONField, ArrayField

# Create your models here. Class is a subclass of django.db.models.Model
class Confessions(models.Model):
    def __str__(self):
        return self.title + self.date + self.id

    id = models.CharField(primary_key=True, max_length=1000)
    title = models.TextField(blank=True, null=True)
    authors = models.TextField(blank=True, null=True)
    date = models.TextField(blank=True, null=True)
    location = models.TextField(blank=True, null=True) 
    summary = models.TextField(blank=True, null=True)

class Headings(models.Model):
    def __str__(self):
        return self.title 
    
    id = models.CharField(primary_key=True, max_length=1000)
    confession = models.ForeignKey(Confessions, on_delete=models.CASCADE)
    heading_number = models.IntegerField()
    title = models.TextField()

class Passages(models.Model):
    def __str__(self):
        return self.passage
    
    id = models.CharField(primary_key=True, max_length=1000)
    confession = models.ForeignKey(Confessions, on_delete=models.CASCADE)
    heading = models.ForeignKey(Headings, on_delete=models.CASCADE)
    passage_number = models.IntegerField()
    heading_number = models.IntegerField(default=0)
    passage = models.TextField()
