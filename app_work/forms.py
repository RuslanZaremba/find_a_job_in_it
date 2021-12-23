from django import forms

from app_work.models import Application, Company


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
