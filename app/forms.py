from django import forms
from app.models import Organization
from app import utils


class SearchForm(forms.Form):
    city = forms.CharField(
        initial='Search by city...',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    state = forms.ChoiceField(
        choices=utils.STATES,
        label='State of Origin',
        widget=forms.Select(attrs={'class': 'form-control'})
    )