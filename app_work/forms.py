from django import forms
from app_work.models import Application, Company, Vacancy


class SentApplicationForm(forms.ModelForm):
    """Форма отклика на вакансию"""

    class Meta:
        model = Application
        fields = ('name', 'phone', 'letter')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control', 'type': 'tel'}),
            'letter': forms.Textarea(attrs={'class': 'form-control', 'rows': '8'})
        }


class CompanyCreateForm(forms.ModelForm):
    """Форма срздания и редактирования компании"""

    class Meta:
        model = Company
        fields = ('name', 'location', 'logo', 'description', 'employee_count')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '4', 'style': 'color:#000;'}),
            'employee_count': forms.NumberInput(attrs={'class': 'form-control'}),
            'logo': forms.FileInput(attrs={'class': 'custom-file-input'}),
        }


class VacancyCreateForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ('title', 'specialty', 'salary_min', 'salary_max', 'skills', 'description')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'specialty': forms.Select(attrs={'class': 'custom-select mr-sm-2', 'id': 'form.vacancy.specialty'}),
            'salary_min': forms.NumberInput(attrs={'class': 'form-control'}),
            'salary_max': forms.NumberInput(attrs={'class': 'form-control'}),
            'skills': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '4', 'style': 'color:#000;'}),
        }
