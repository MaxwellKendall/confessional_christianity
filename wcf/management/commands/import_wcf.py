import os
import re
from django.core.management.base import BaseCommand
from wcf.models import wcf

class Command(BaseCommand):
    help = 'Populates the DB with the Westminster Confession of Faith'
    def parse_title(self, data):
        self.stdout.write(data)
    def parse_paragraph(self, data):
        self.stdout.write(data)
    def parse_proof(self, data):
        self.stdout.write(data)
    def build_chapter(self, data):
        return {
            'title': self.parse_title(data),
            'paragraphs': self.parse_paragraph(data),
            'id': 'WCF_123'
        }
    def write_to_db(self, chapter):
        print("eventually will save this to the db", chapter)

    def handle(self, *args, **options):
        # import logic goes here
        wcf = open("confessional_christianity_api/data/WCF.txt").read().split('__WCF_CHAPTER__')
        for chapter in wcf[1:]:
            arr = chapter.replace('\n', '').split(' ')
            titleIndex = arr.index('__WCF_PARAGRAPH__')
            print(' '.join(arr[:titleIndex]))
        self.stdout.write(self.style.SUCCESS('Success!!'))

# https://docs.djangoproject.com/en/dev/howto/custom-management-commands/ & https://eli.thegreenplace.net/2014/02/15/programmatically-populating-a-django-database
