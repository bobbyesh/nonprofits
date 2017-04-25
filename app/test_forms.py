from django.test import TestCase, RequestFactory
from app.forms import SearchForm


class CitySearchFormTestCase(TestCase):

    def test_city_search(self):
        data = {'city': 'Portland'}
        factory = RequestFactory()
        request = factory.post('/', data)
        form = SearchForm(request.POST)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['city'], data['city'])