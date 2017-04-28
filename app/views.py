from django.views.generic import TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from app.models import Organization
from app.forms import SearchForm


class IndexView(TemplateView):
    template_name = 'app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        organization_list = Organization.objects.all()
        if self.request.GET:
            state = self.request.GET.get('state')
            if state:
                organization_list = organization_list.filter(state=state)

            city = self.request.GET.get('city')
            # Don't filter by city if the user hits submit without changing the placeholder
            if city and city != 'Search by city...':
                organization_list = organization_list.filter(city=city.upper())
            zip_code = self.request.GET.get('zip_code')

            if zip_code:
                organization_list = organization_list.filter(zip_code=zip_code)

        organization_list = organization_list.order_by('id')
        organization_list = self.get_pagination(organization_list)

        context['organization_list'] = organization_list
        context['current_params'] = self.get_params_string()
        context['search_form'] = SearchForm()
        context['GOOGLE_MAPS_API_KEY'] = settings.GOOGLE_MAPS_API_KEY
        return context

    def get_pagination(self, queryset):
        paginator = Paginator(queryset, 25)
        page = self.request.GET.get('page')
        try:
            queryset = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            queryset = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            queryset = paginator.page(paginator.num_pages)

        return queryset

    def get_params_string(self):
        params = dict(self.request.GET)
        if 'page' in params:
            params.pop('page')
        template = '&{}={}'
        ret = ''
        for key, vals in params.items():
            for val in vals:
                ret += template.format(key, val)
        return ret


class AboutView(TemplateView):
    template_name = 'app/about.html'