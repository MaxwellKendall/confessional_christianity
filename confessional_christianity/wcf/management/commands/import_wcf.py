import os
import re
from django.core.management.base import BaseCommand
from django.contrib.postgres.fields import JSONField, ArrayField

from wcf.models import wcf

# parsing scripture proof texts
regexString = "((?:\d\s[A-Z][a-z]*|[A-Z][a-z]*)(?:\.\s|\s)(?:[0-9]*:[0-9]*-[0-9]*\.|[0-9]*:[0-9]*)(?:\.|(?:,\s\d*)*))"

class Command(BaseCommand):
    help = 'Populates the DB with the Westminster Confession of Faith :bang!:'

    def remove_numbers(self, char):
        return char != "1." and char != "2." and char != "3." and char != "4." and char != "5." and char != "6." and char != "7." and char != "8." and char != "9." and char != "10." and char != "11." and char != "12." and char != "13." and char != "14." and char != "15." and char != "16."
    def parse_title(self, arrayOfTitleWords):
        return ' '.join(arrayOfTitleWords).strip()
    def parse_paragraphs(self, arrayOfParagraphs):
        paragraphsForChapter = []
        for paragraph in arrayOfParagraphs:
            arrayOfWordsInParagraph = list(filter(lambda item: item != '__WCF_SCRIPTURE_REF' and self.remove_numbers(item), paragraph.strip().split(' ')))
            paragraphsForChapter.append(' '.join(arrayOfWordsInParagraph).strip())
        return paragraphsForChapter
    def parse_proofs(self, arrayOfProofs):
        proof_map = {}
        for proof in arrayOfProofs:
            parsedProof = proof.strip()
            proofReference = parsedProof[0]
            proofCitations = re.findall(regexString, parsedProof[2:])
            proof_map[proofReference] = parsedProof[2:].strip()
            print("**********", proofCitations)
        return proof_map
    def build_chapter(self, data):
        firstParagraphIndex = data.index('__WCF_PARAGRAPH__')
        firstProofIndex = data.index('WCF_PROOF') - 1
        arrayOfProofs = ' '.join(data[firstProofIndex + 1:]).strip().split('WCF_PROOF')[1:]
        chapterAsString = ' '.join(data[firstParagraphIndex:firstProofIndex]).strip()
        arrayOfParagraphs = chapterAsString.split('__WCF_PARAGRAPH__')[1:]
        return {
            'paragraphs': self.parse_paragraphs(arrayOfParagraphs),
            'title': self.parse_title(data[:firstParagraphIndex]),
            'proofs': self.parse_proofs(arrayOfProofs)
        }
    def write_to_db(self, wcfArray):
        for index, chapter in enumerate(wcfArray):
            newChapter = wcf(id=chapter['id'], chapter_number=index + 1, title=chapter['title'], proofs=chapter['proofs'], paragraphs=chapter['paragraphs'])
            successMsg = "The chapter of the Confession entitled " + newChapter.title + " was successfully saved to database!"
            self.stdout.write(self.style.SUCCESS(successMsg))
            newChapter.save()
        successMsg = "All " + str(len(wcfArray)) + " chapters of the Westminster Confession of Faith have been successfully saved to the database!"
        self.stdout.write(self.style.SUCCESS(successMsg))

    def handle(self, *args, **options):
        arrayOfWcfChapters = []
        wcf = open("confessional_christianity/confessional_christianity_api/data/WCF.txt").read().split('__WCF_CHAPTER__')
        for index, chapter in enumerate(wcf[1:]):
            obj = self.build_chapter(chapter.replace('\n', ' ').split(' '))
            obj['id'] = 'WCF_' + str(index + 1)
            arrayOfWcfChapters.append(obj)
        self.write_to_db(arrayOfWcfChapters)
        self.stdout.write(self.style.SUCCESS('Success!!'))

# https://docs.djangoproject.com/en/dev/howto/custom-management-commands/ & https://eli.thegreenplace.net/2014/02/15/programmatically-populating-a-django-database
