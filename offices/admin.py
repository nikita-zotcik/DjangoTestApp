from django.contrib import admin

from offices.forms import CompanyForm
from offices.models import Office, Company

admin.site.register(Office)


class CompanyAdmin(admin.ModelAdmin):
    """
    Admin Class for 'Company'.
    """
    fieldsets = [
        ('Company details', {'fields': ('name', 'headquarter')})
    ]
    form = CompanyForm


admin.site.register(Company, CompanyAdmin)