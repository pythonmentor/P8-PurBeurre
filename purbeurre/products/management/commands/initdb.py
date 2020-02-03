'''module to initiate'''

from django.core import management
from django.core.management.base import BaseCommand

from ...off_api.main import Call


class Command(BaseCommand):
    help = 'makes migrations and load api data'

    def handle(self, *args, **options):
        management.call_command('makemigrations')
        management.call_command('migrate')
        Call.insert_data()
