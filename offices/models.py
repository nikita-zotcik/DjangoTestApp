from django.core.exceptions import ValidationError
from django.db import models


class Office(models.Model):
    country = models.CharField('Country', max_length=256, blank=True)
    street = models.CharField('Street', max_length=256, blank=True)
    postal_code = models.CharField('Postal Code', max_length=32, blank=True)
    city = models.CharField('City', max_length=128, blank=True, null=True)
    company = models.ForeignKey('offices.Company', on_delete=models.SET_NULL,
                                related_name='offices', blank=True, null=True)
    monthly_rent = models.DecimalField(decimal_places=2, max_digits=10,
                                       blank=True, null=True)

    class Meta:
        verbose_name_plural = "offices"

    def has_is_headquarter(self):
        return hasattr(self, 'is_headquarter')

    def clean(self, *args, **kwargs):
        if hasattr(self, 'is_headquarter') and self.company:
            if self.is_headquarter != self.company:
                raise ValidationError(
                    "Company of Headquarter Office can't be changed"
                )
        super(Office, self).clean(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.full_clean(exclude='is_headquarter')
        super(Office, self).save(*args, **kwargs)

    def __str__(self):
        return "{}, {} str., {}. {}".format(self.city,
                                            self.street,
                                            self.postal_code,
                                            self.country)


class Company(models.Model):
    name = models.CharField('Name', max_length=300)
    headquarter = models.OneToOneField(Office, on_delete=models.CASCADE,
                                       related_name="is_headquarter", default=None)

    class Meta:
        verbose_name_plural = 'companies'

    def has_headquarter(self):
        return hasattr(self, 'headquarter')

    def clean(self, *args, **kwargs):
        if not self.has_headquarter():
            raise ValidationError(
                "Company always should have a headquarter"
            )
        is_new_company_and_office = not self.id and not self.headquarter.company
        office_belongs_to_company = (not self.headquarter.company) or (self.id == self.headquarter.company.id)
        if is_new_company_and_office or office_belongs_to_company:
            super(Company, self).clean(*args, **kwargs)
        else:
            raise ValidationError(
                "Headquarter Office should belong to company"
            )

    def save(self, *args, **kwargs):
        self.full_clean()
        super(Company, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
