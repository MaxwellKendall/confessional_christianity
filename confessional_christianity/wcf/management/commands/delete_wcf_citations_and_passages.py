import os
import re
from django.core.management.base import BaseCommand
from django.contrib.postgres.fields import JSONField, ArrayField

from confessions.models import Passages, Headings, Confessions
from citations.models import Citations
from wcf.models import wcf

class Command(BaseCommand):
    help = 'Quick Deletion of records'

    def handle(self, *args, **options):
        Citations.objects.all().delete()
        Passages.objects.all().delete()
        Headings.objects.all().delete()
        wcf.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Success!!'))

# https://docs.djangoproject.com/en/dev/howto/custom-management-commands/ & https://eli.thegreenplace.net/2014/02/15/programmatically-populating-a-django-database
