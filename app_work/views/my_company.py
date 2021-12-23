from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, CreateView, UpdateView

from app_work.forms import CompanyCreateForm
from app_work.models import Company


class CompanyLetStartView(TemplateView):
    template_name = 'app_work/company/company-create.html'
    extra_context = {'title': 'Добавьте кампанию'}


class CompanyCreateView(CreateView):
    model = Company
    form_class = CompanyCreateForm
    template_name = 'app_work/company/company-edit.html'
    extra_context = {'title': 'Редактирование компании'}
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(CompanyCreateView, self).form_valid(form)


class CompanyEditView(UpdateView):
    model = Company
    form_class = CompanyCreateForm
    template_name = 'app_work/company/company-edit.html'
    # success_url = f'/mycompany/{str(Company.id)}'
