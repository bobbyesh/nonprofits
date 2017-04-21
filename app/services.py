import requests
from django.utils.dateparse import parse_datetime
from django.conf import settings
import pytz
from app.models import Organization


FIELDS = [
    'business_name',
    'associated_name_type',
    'entity_type',
    'nonprofit_type',
    'zip_code',
    'address',
    'city',
    'registry_number',
    'registry_date',
    'state',
]


def load_models() -> None:
    data_set = get_api_data()
    for data in data_set:
        Organization.objects.create(**data)


def get_api_data() -> dict:
    url = 'https://data.oregon.gov/resource/8qki-3wtm.json'
    headers = {'X-App-Token': settings.APP_TOKEN}
    response = requests.get(url, headers=headers)
    data_set = response.json()
    return_list = []
    for data in data_set:
        return_data = dict()
        registry_date = data.pop('registry_date')
        registry_date = parse_datetime(registry_date)
        registry_date = pytz.timezone('America/Los_Angeles').localize(registry_date, is_dst=None)
        data['registry_date'] = registry_date
        for field in FIELDS:
            return_data[field] = data.get(field)

        if not return_data['address']:
            return_data['address'] = ''

        return_list.append(return_data)
    return return_list


if __name__ == '__main__':
    data = get_api_data()
    print(len(data))