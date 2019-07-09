from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.db import IntegrityError
from django.test import TestCase

from offices.models import Office, Company


class CompanyModelTest(TestCase):

    def set_up(self):
        self.first_office = Office.objects.create(country="test",
                                                  street="test",
                                                  postal_code="123qwe",
                                                  city="test",
                                                  monthly_rent=12)
        self.second_office = Office.objects.create(country="test",
                                                   street="test",
                                                   postal_code="123qwe",
                                                   city="test",
                                                   monthly_rent=12)

    def test_company_should_always_have_a_headquarter(self):
        self.assertRaises(ValidationError,
                          lambda: Company.objects.create(name="test"))

    def test_company_should_always_have_exact_one_headquarter(self):
        self.set_up()
        test_company = Company.objects.create(name='test1',
                                              headquarter=self.first_office)

        def set_another_headquarter():
            test_company.headquarter = self.second_office
            test_company.save()
            return Office.objects.get(
                pk=self.first_office.id).has_is_headquarter()

        self.assertEqual(False, set_another_headquarter())

    def test_company_cant_exist_without_headquarter(self):
        self.set_up()
        test_company = Company.objects.create(name='test1',
                                              headquarter=self.first_office)
        Office.delete(self.first_office)
        self.assertRaises(ObjectDoesNotExist,
                          lambda: Office.objects.get(pk=test_company.id))

    def test_headquarter_of_company_always_belongs_its_offices(self):
        self.set_up()
        test_company = Company.objects.create(name='test1',
                                              headquarter=self.first_office)
        Company.objects.create(name='test2',
                               headquarter=self.second_office)

        def change_company_of_office():
            self.second_office.company = test_company
            self.second_office.save()

        self.assertRaises(ValidationError, lambda: change_company_of_office())

    def test_one_headquarter_can_belong_only_to_one_company(self):
        self.set_up()
        Company.objects.create(name='test1',
                               headquarter=self.first_office)

        def set_the_same_office_as_headsquarter():
            Company.objects.create(name='test2',
                                   headquarter=self.first_office)

        self.assertRaises(ValidationError, lambda: set_the_same_office_as_headsquarter())
