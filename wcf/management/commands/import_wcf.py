from django.core.management.base import BaseCommand
from wcf.models import wcf


class Command(BaseCommand):
    help = 'Populates the DB with the Westminster Confession of Faith'

    def handle(self, *args, **options):
        # import logic goes here
        self.stdout.write(self.style.SUCCESS('Success!!'))

# https://docs.djangoproject.com/en/dev/howto/custom-management-commands/ & https://eli.thegreenplace.net/2014/02/15/programmatically-populating-a-django-database