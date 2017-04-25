from django.core.management.base import BaseCommand, CommandError
from app.models import Organization
from app.services import get_api_data, get_coordinates


class Command(BaseCommand):
    help = 'Loads the DB with organization data'

    def add_arguments(self, parser):
        parser.add_argument('--empty', action='store_true', default=False)

    def handle(self, *args, **options):
        if options['empty']:
            Organization.objects.all().delete()

        else:
            for data in get_api_data():
                organization = Organization(**data)
                latitude, longitude = get_coordinates(organization.full_address())
                organization.latitude = latitude
                organization.longitude = longitude
                organization.save()
