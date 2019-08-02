import os
import re
from django.core.management.base import BaseCommand
from wcf.models import wcf

class Command(BaseCommand):
    help = 'Populates the DB with the Westminster Confession of Faith'
    def parse_title(self, arrayOfTitleWords):
        return ' '.join(arrayOfTitleWords).strip()
    def parse_paragraphs(self, arrayOfParagraphs):
        rtrn = []
        for paragraph in arrayOfParagraphs:
            arrayOfWordsInParagraph = list(filter(lambda item: item != '__WCF_SCRIPTURE_REF', paragraph.split(' ')))
            rtrn.append(' '.join(arrayOfWordsInParagraph))
        return rtrn
    def parse_proof(self, data):
        self.stdout.write(data)
    def build_chapter(self, data):
        # firstParagraph is right after end of the Chapter title
        print("DATA *****", data)
        firstParagraphIndex = data.index('__WCF_PARAGRAPH__')
        firstProofIndex = data.index('WCF_PROOF') - 1
        chapterAsString = ' '.join(data[firstParagraphIndex:firstProofIndex]).strip()
        arrayOfParagraphs = chapterAsString.split('__WCF_PARAGRAPH__')[1:]
        return {
            'paragraphs': self.parse_paragraphs(arrayOfParagraphs),
            'title': self.parse_title(data[:firstParagraphIndex]),
            'proofs': 'blah blah',
            'id': 'WCF_123'
        }
    def write_to_db(self, chapter):
        print("eventually will save this to the db", chapter)

    def handle(self, *args, **options):
        rtrn = []
        # import logic goes here
        wcf = open("confessional_christianity_api/data/WCF.txt").read().split('__WCF_CHAPTER__')
        for index, chapter in enumerate(wcf[1:]):
            print("CHAPTER", index)
            obj = self.build_chapter(chapter.replace('\n', '').split(' '))
            obj['id'] = 'WCF_' + str(index + 1)
            rtrn.append(obj)
        print(rtrn[30])
        self.stdout.write(self.style.SUCCESS('Success!!'))

# https://docs.djangoproject.com/en/dev/howto/custom-management-commands/ & https://eli.thegreenplace.net/2014/02/15/programmatically-populating-a-django-database
