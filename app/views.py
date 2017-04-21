from django.views.generic import TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from app.models import Organization


class IndexView(TemplateView):
    template_name = 'app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        organization_list = self.get_queryset()
        paginator = Paginator(organization_list, 25)
        page = self.request.GET.get('page')
        try:
            organization_list = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            organization_list = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            organization_list = paginator.page(paginator.num_pages)
        context['organization_list'] = organization_list
        context['current_params'] = self.get_params_string()
        return context

    def get_queryset(self):
        queryset = Organization.objects.all().order_by('id')
        queryset = self.filter_by_param('city', queryset)
        queryset = self.filter_by_param('state', queryset)
        queryset = self.filter_by_param('zip_code', queryset)
        return queryset

    def filter_by_param(self, param, queryset):
        if param in self.request.GET:
            field = self.request.GET.get(param)
            field = field.upper()
            kwarg = {param: field}
            return queryset.filter(**kwarg)
        else:
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