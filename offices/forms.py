from django import forms
from offices.models import Office, Company


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['headquarter']

    def __init__(self, *args, **kwargs):
        super(CompanyForm, self).__init__(*args, **kwargs)
        self.fields['headquarter'].queryset = Office.objects.filter(
            company=self.instance.id)
