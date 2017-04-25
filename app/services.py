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


def get_api_data() -> list:
    url = 'https://data.oregon.gov/resource/8qki-3wtm.json'
    headers = {'X-App-Token': settings.APP_TOKEN}
    response = requests.get(url, headers=headers)
    data_set = response.json()
    return_list = []
    already_used_names = set()
    for data in data_set:
        return_data = dict()
        name = data.get('business_name')
        if name not in already_used_names:
            registry_date = data.pop('registry_date')
            registry_date = parse_datetime(registry_date)
            registry_date = pytz.timezone('America/Los_Angeles').localize(registry_date, is_dst=None)
            data['registry_date'] = registry_date
            for field in FIELDS:
                return_data[field] = data.get(field)

            if not return_data['address']:
                return_data['address'] = ''

            return_list.append(return_data)

        already_used_names.add(name)

    return return_list


def get_coordinates(address):
    url = "https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s" % (address, settings.GOOGLE_MAPS_API_KEY)
    response = requests.get(url)
    results = response.json()['results']
    if len(results) > 0:
        location = results[0]['geometry']['location']
        return location['lat'], location['lng']
    else:
        return None, None