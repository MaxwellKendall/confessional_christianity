import os
import re
from django.core.management.base import BaseCommand
from django.contrib.postgres.fields import JSONField, ArrayField

from confessions.models import Confessions

# parsing scripture proof texts
FindScriptureBook = "(?P<book>((1.{1}[A-Z][a-z]*)|(2\s[A-Z][a-z]*))|[A-Z][a-z]*)"
FindScriptureVerses = "(?P<verse>(\d{1,3}:\d{1,3}-\d{1,3}|\d{1,3}:\d{1,3})(:\d{1,3}|(,\s\d{1,3}|\4-\d{1,3})*|\b))"
regexString = "(?P<citation>{book}(\.\s|\s){verse})".format(book=FindScriptureBook, verse=FindScriptureVerses)

class Command(BaseCommand):
    help = 'Populates the DB Table "Confessions" with historical details about the Westminster Confession of Faith :bang!:'

    def get_data_by_annotations(self, data, beginningAnnotation, endAnnotation):
        beginingIndex = data.index(beginningAnnotation)
        endIndex = data.index(endAnnotation)
        if beginningAnnotation == '__CONFESSION_SUMMARY__':
            return ''.join(data[beginingIndex:]).replace(beginningAnnotation, '')
        return ''.join(data[beginingIndex:endIndex]).replace(beginningAnnotation, '').strip()

    def handle(self, *args, **options):
        arrayOfWcfChapters = []
        wcfSummary = open("confessional_christianity/confessional_christianity_api/data/WCF_Summary.txt").read().split("\n")
        confessionId = self.get_data_by_annotations(wcfSummary, '__CONFESSION_ID__', '__CONFESSION_TITLE__')
        title = self.get_data_by_annotations(wcfSummary, '__CONFESSION_TITLE__', '__CONFESSION_AUTHORS__')
        authors = self.get_data_by_annotations(wcfSummary, '__CONFESSION_AUTHORS__', '__CONFESSION_LOCATION__')
        location = self.get_data_by_annotations(wcfSummary, '__CONFESSION_LOCATION__', '__CONFESSION_DATE__')
        date = self.get_data_by_annotations(wcfSummary, '__CONFESSION_DATE__', '__CONFESSION_SUMMARY__')
        summary = self.get_data_by_annotations(wcfSummary, '__CONFESSION_SUMMARY__', '')
        print(confessionId)
        wcf = Confessions(id=confessionId, title=title, authors=authors, location=location, date=date, summary=summary)
        wcf.save()
        successMsg = "Historical Details like Date (" + date + ") and authors (" +  authors + ") chapters of the Westminster Confession of Faith have been successfully saved to the database!"
        self.stdout.write(self.style.SUCCESS('Success!!'))

# https://docs.djangoproject.com/en/dev/howto/custom-management-commands/ & https://eli.thegreenplace.net/2014/02/15/programmatically-populating-a-django-database
