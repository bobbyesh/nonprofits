from django.views.generic import TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from app.models import Organization



class IndexView(TemplateView):
    template_name = 'app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        organization_list = Organization.objects.all().order_by('id')
        paginator = Paginator(organization_list, 25)
        page = kwargs.get('page')
        try:
            organization_list = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            organization_list = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            organization_list = paginator.page(paginator.num_pages)
        context['organization_list'] = organization_list
        return context