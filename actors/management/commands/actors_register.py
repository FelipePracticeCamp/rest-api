from django.core.management.base import BaseCommand
import csv



class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            'file_name',
            type=str,
            help='Nome do arquivo',
        )

    def handle(self, *args, **options):
        file_name = options['file_name']
        dados = csv.DictReader(file_name)
        
        