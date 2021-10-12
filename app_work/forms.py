from django import forms

from app_work.models import Application


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
