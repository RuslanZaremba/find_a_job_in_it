from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from app_work.views.public import IndexView, VacanciesListView, CompanyDetailView, VacancyDetailView, \
    VacanciesByCategoryView, SuccessSentApplication
from app_work.views.my_company import CompanyLetStartView, CompanyCreateView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('vacancies/', VacanciesListView.as_view(), name='vacancies'),
    path('company/<int:pk>/', CompanyDetailView.as_view(), name='company'),
    path('vacancies/<int:pk>/', VacancyDetailView.as_view(), name='vacancy'),
    path('vacancies/cat/<str:specialty>', VacanciesByCategoryView.as_view(), name='vacancy_by_category'),
    path('vacancies/<int:pk>/send/', SuccessSentApplication.as_view(), name='success_sent_application'),

    path('mycompany/letsstart/', CompanyLetStartView.as_view(), name='company_let_start'),
    path('mycompany/create/', CompanyCreateView.as_view(), name='company_create')
]
