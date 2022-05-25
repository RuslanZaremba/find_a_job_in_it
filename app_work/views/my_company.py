from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, CreateView, UpdateView, ListView

from app_work.forms import CompanyCreateForm, VacancyCreateForm
from app_work.models import Company, Vacancy


class CompanyLetStartView(TemplateView):
    template_name = 'app_work/company/company-create.html'
    extra_context = {'title': 'Добавьте кампанию'}


class CompanyCreateView(CreateView):
    model = Company
    form_class = CompanyCreateForm
    template_name = 'app_work/company/company-edit.html'
    extra_context = {'title': 'Редактирование компании'}

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(CompanyCreateView, self).form_valid(form)


class CompanyEditView(UpdateView):
    model = Company
    form_class = CompanyCreateForm
    template_name = 'app_work/company/company-edit.html'


class MyCompanyVacancies(ListView):
    model = Vacancy
    template_name = 'app_work/company/vacancy-list.html'
    context_object_name = 'vacancies'
    extra_context = {'title': 'Все вакансии вашей кампании'}

    def get_queryset(self):
        return Vacancy.objects.filter(company__owner=self.request.user.id)


class MyCompanyCreateVacancy(CreateView):
    form_class = VacancyCreateForm
    template_name = 'app_work/company/vacancy-edit.html'
    extra_context = {'title': 'Редактирование вакансии'}
    success_url = reverse_lazy('index')

    # def form_valid(self, form):
    #     form.instance.company = self.request.company
    #     messages.success(self.request, 'The city has been added to the list of visited places, thank you')
    #     return super().form_valid(form)
