"""conf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from app_work import views
from app_work.views import IndexView, VacanciesListView, CompanyDetailView, VacancyDetailView, VacanciesByCategoryView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('vacancies/', VacanciesListView.as_view(), name='vacancies'),
    path('companies/<int:pk>/', CompanyDetailView.as_view(), name='company'),
    path('vacancy/<int:pk>/', VacancyDetailView.as_view(), name='vacancy'),
    path('vacancies/cat/<str:specialty>', VacanciesByCategoryView.as_view(), name='vacancy_by_category'),
]

handler404 = views.custom_handler404
handler500 = views.custom_handler500
