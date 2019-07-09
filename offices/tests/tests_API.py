import json

from rest_framework import status
from rest_framework.test import APITestCase, RequestsClient
from offices.models import Office, Company
from offices.api.views import CompanyViewSet
from django.urls import reverse


class CompanyViewSetTestCase(APITestCase):

    def test_company_creation_with_headquarter(self):
        data = {
            "headquarter": {
                "country": "test",
                "street": "test",
                "postal_code": "test",
                "city": "test",
                "monthly_rent": 100
            },
            "headquarter_id": None,
            "name": "test"
        }
        client = RequestsClient()
        response = client.post("http://testserver/api/company/", json=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_show_company_along_with_headquarter_data(self):
        self.office = Office.objects.create(country="test",
                                            street="test",
                                            postal_code="123qwe",
                                            city="test",
                                            monthly_rent=12)
        self.company = Company.objects.create(name='Company',
                                              headquarter=self.office)

        initial_string = "{}: {}, {}, {}".format(self.company.id,
                                                 self.office.street,
                                                 self.office.postal_code,
                                                 self.office.city)

        response = self.client.get("/api/company/1/".format(self.company.id))
        street = response.json().get('street', None)
        postal_code = response.json().get('postal_code', None)
        city = response.json().get('city', None)
        company_id = response.json().get('id', None)

        result_string = "{}: {}, {}, {}".format(company_id,
                                                street,
                                                postal_code,
                                                city)
        self.assertEqual(initial_string, result_string)

    def test_company_headquarter_can_be_changed(self):
        self.office = Office.objects.create(country="test",
                                            street="test",
                                            postal_code="123qwe",
                                            city="test",
                                            monthly_rent=12)

        self.secondOffice = Office.objects.create(country="second",
                                                  street="second",
                                                  postal_code="second",
                                                  city="second",
                                                  monthly_rent=500)
        self.company = Company.objects.create(name='TTT',
                                              headquarter=self.office)
        data = {
            "name": self.company.name,
            "headquarter_id": self.secondOffice.id
        }
        response = self.client.put(reverse("company-detail",
                                           kwargs={"pk": self.company.id}),
                                   data)
        postal_code = response.json().get('postal_code')

        self.assertEqual(self.secondOffice.postal_code, postal_code)


class OfficeListViewTestCase(APITestCase):

    def setUp(self):
        self.office = Office.objects.create(country="test",
                                            street="test",
                                            postal_code="123qwe",
                                            city="test",
                                            monthly_rent=12)

        self.secondOffice = Office.objects.create(country="second",
                                                  street="second",
                                                  postal_code="second",
                                                  city="second",
                                                  monthly_rent=500)
        self.company = Company.objects.create(name='TTT',
                                              headquarter=self.office)
        self.secondOffice.company = self.company
        self.secondOffice.save()

    def test_company_offices_list(self):
        response = self.client.get(reverse("company-offices",
                                           kwargs={"pk": self.company.id}))
        self.assertEqual(len(response.json().get('offices')), 2)

    def test_total_sum_offices_rent(self):
        response = self.client.get(reverse("company-offices",
                                           kwargs={"pk": self.company.id}))
        offices_sum = self.office.monthly_rent + self.secondOffice.monthly_rent

        self.assertEqual(response.json().get('total_rent'), offices_sum)


class OfficeCreateDeleteUpdateTestCase(APITestCase):
    def setUp(self):
        self.office = Office.objects.create(country="test",
                                            street="test",
                                            postal_code="123qwe",
                                            city="test",
                                            monthly_rent=12)

        self.secondOffice = Office.objects.create(country="second",
                                                  street="second",
                                                  postal_code="second",
                                                  city="second",
                                                  monthly_rent=500)
        self.company = Company.objects.create(name='TTT',
                                              headquarter=self.office)
        self.secondOffice.company = self.company
        self.secondOffice.save()

    def test_create_office_for_company(self):
        data = {

            "country": "test",
            "street": "test",
            "postal_code": "test",
            "city": "test",
            "monthly_rent": 100
        }
        client = RequestsClient()
        response = client.post(
            "http://testserver/api/company/{}/offices/create"
                .format(self.company.id), json=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_office(self):
        response = self.client.delete(reverse("offices-delete",
                                              kwargs={"pk": self.office.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
