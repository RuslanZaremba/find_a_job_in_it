from django.views.generic import TemplateView, CreateView


class CompanyLetStartView(TemplateView):
    template_name = 'app_work/company/company-create.html'


class CompanyCreateView(CreateView):
    pass
