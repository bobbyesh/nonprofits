from django.test import TestCase
from django.utils.dateparse import parse_datetime
from app.models import Organization
import pytz


class OrganizationTestCase(TestCase):
    def test_create(self):
        data = {
            "entity_type": "DOMESTIC NONPROFIT CORPORATION",
            "nonprofit_type": "PUBLIC BENEFIT",
            "zip_code": "97227",
            "address": "3635 N WILLIAMS AVE",
            "city": "PORTLAND",
            "registry_number": "25228594",
            "registry_date": "2004-11-16 00:00:00",
            "state": "OR",
            "associated_name_type": "PRINCIPAL PLACE OF BUSINESS",
            "business_name": "LIFE CHANGE OUTREACH SERVICES, INC."
        }

        registry_date = data.pop('registry_date')
        registry_date = parse_datetime(registry_date)
        registry_date = pytz.timezone('America/Los_Angeles').localize(registry_date, is_dst=None)
        data['registry_date'] = registry_date
        Organization.objects.create(**data)
        queryset = Organization.objects.all()
        self.assertEquals(len(queryset), 1)

