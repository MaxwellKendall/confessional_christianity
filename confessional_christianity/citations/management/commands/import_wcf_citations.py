import os
import re
from django.core.management.base import BaseCommand
from django.contrib.postgres.fields import JSONField, ArrayField

from citations.models import Citations
from citations.abbrev import wcf as wcf_abbrev_map

# parsing scripture proof texts
FindScriptureBook = "(?P<book>((1.{1}[A-Z][a-z]*)|(2\s[A-Z][a-z]*))|[A-Z][a-z]*)"
FindScriptureVerses = "(?P<verse>(\d{1,3}:\d{1,3}-\d{1,3}|\d{1,3}:\d{1,3})(:\d{1,3}|(,\s\d{1,3}|\4-\d{1,3})*|\b))"
regexString = "(?P<citation>{book}(\.\s|\s){verse})".format(book=FindScriptureBook, verse=FindScriptureVerses)

class Command(BaseCommand):
    help = 'Populates the DB Table "Citations" with the Scripture Citations from the Westminster Confession of Faith :bang!:'

    def remove_numbers(self, char):
            return char != "1." and char != "2." and char != "3." and char != "4." and char != "5." and char != "6." and char != "7." and char != "8." and char != "9." and char != "10." and char != "11." and char != "12." and char != "13." and char != "14." and char != "15." and char != "16."

    def get_citation_ids_by_paragraph(self, arrayOfParagraphs):
        citationIdsByParagraph = {}
        for index, paragraph in arrayOfParagraphs:
            citationIdsInParagraph = []
            arrayOfWordsInParagraph = paragraph.strip().split(' ')
            paragraphNumber = index + 1
            for index, word in arrayOfWordsInParagraph:
                if word == '__WCF_SCRIPTURE_REF':
                    print(arrayOfWordsInParagraph[index + 1])
                    citationIdsInParagraph.append(arrayOfWordsInParagraph[index + 1])
            citationIdsByParagraph[paragraphNumber] = citationIdsInParagraph
        return citationIdsByParagraph

    def parse_proofs(self, arrayOfProofs):
        proof_map = {}
            
        for proof in arrayOfProofs:
            parsedProof = proof.strip()
            proofReference = parsedProof[0]
            proofCitations = re.compile(regexString).finditer(parsedProof[2:])
            citations = []
            for m in proofCitations:
                book = wcf_abbrev_map[m.group("book")]
                citations.append(book + " " + m.group("verse"))
            proof_map[proofReference] = citations
            print(proof_map[proofReference])
        return proof_map

    def get_citations_for_chapter(self, chapter, referenceId):
        firstParagraphIndex = chapter.index('__WCF_PARAGRAPH__')
        firstProofIndex = chapter.index('WCF_PROOF') - 1
        arrayOfProofs = ' '.join(chapter[firstProofIndex + 1:]).strip().split('WCF_PROOF')[1:]
        chapterAsString = ' '.join(chapter[firstParagraphIndex:firstProofIndex]).strip()
        arrayOfParagraphs = chapterAsString.split('__WCF_PARAGRAPH__')[1:]
        citationIdsByParagraph = self.get_citation_ids_by_paragraph(arrayOfParagraphs)
        scriptureReferencesByCitationId = self.parse_proofs(arrayOfProofs)
        citations = []
        for paragraph, in list(citationIdsByParagraph):
        # assuming there's not two citations with the id "a" for a given chapter... ? 
            for citationID in citationIdsByParagraph[paragraph]:
                scriptureReference = scriptureReferencesByCitationId[citationID]
                citations.append({
                    "id": referenceId + "_" + paragraph + "_" + citationID,
                    "referenceIdentifier": citationID,
                    "scripture": scriptureReference,
                    "confession_id": "WCF",
                    "headingId": citationID,
                    "tags": [],
                    "passage_id": citationID + "_" + paragraph
                })

        return citations

    def write_to_db(self, citationObj):
        print("*****", citationObj)
        newCitation = Citations(id=citationObj['id'], confession_id=citationObj['confessionId'], heading_id=citationObj[headingId], referenceIdentifier=index + 1, scripture=chapter['paragraphs'])
        # newCitation.save()
        successMsg = "Citation " + newCitation.id + " was successfully saved to database!"
        self.stdout.write(self.style.SUCCESS(successMsg))

    def handle(self, *args, **options):
        arrayOfWcfChapters = []
        wcf = open("confessional_christianity/confessional_christianity_api/data/WCF.txt").read().split('__WCF_CHAPTER__')
        for index, chapter in enumerate(wcf[1:]):
            citationId = "WCF_" + index + 1
            chapter = chapter.replace('\n', ' ').split(' ')
            self.get_citations_for_chapter(chapter, citationId)
            # obj = self.build_chapter()
            # obj['id'] = 'WCF_' + str(index + 1)
            # arrayOfWcfChapters.append(obj)
        # self.write_to_db(arrayOfWcfChapters)
        self.stdout.write(self.style.SUCCESS('Success!!'))

# https://docs.djangoproject.com/en/dev/howto/custom-management-commands/ & https://eli.thegreenplace.net/2014/02/15/programmatically-populating-a-django-database
