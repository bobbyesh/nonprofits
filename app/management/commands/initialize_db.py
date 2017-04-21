from django.core.management.base import BaseCommand, CommandError
from app.models import Organization
from app.services import get_api_data


class Command(BaseCommand):
    help = 'Loads the DB with organization data'

    def add_arguments(self, parser):
        parser.add_argument('--empty', action='store_true', default=False)

    def handle(self, *args, **options):
        if options['empty']:
            Organization.objects.all().delete()

        else:
            data_list = get_api_data()
            for data in data_list:
                print('name:', data['business_name'])
                try:
                    Organization.objects.create(**data)
                except:
                    print(data)
                    raise