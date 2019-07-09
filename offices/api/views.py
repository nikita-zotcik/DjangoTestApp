from rest_framework import viewsets, generics
from rest_framework.response import Response
from django.db.models import Sum

from offices.api.serializers import OfficeSerializer, CompanySerializer
from offices.models import Office, Company


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class OfficeListAPIView(generics.ListAPIView):
    serializer_class = OfficeSerializer

    def get_queryset(self):
        kwargs_company = self.kwargs.get('pk')
        if kwargs_company:
            return Office.objects.filter(company=kwargs_company)
        return Office.objects.all()

    def get(self, request, *args, **kwargs):
        offices = self.get_queryset()
        serializer = self.serializer_class(offices, many=True)
        if kwargs.get('pk', None):
            total_rent = offices.aggregate(Sum('monthly_rent'))['monthly_rent__sum']
            return Response(
                {
                    'total_rent': total_rent if total_rent else 0,
                    'offices': serializer.data
                }
            )
        return Response(serializer.data)


class RetrieveOfficesView(generics.RetrieveAPIView):
    serializer_class = OfficeSerializer
    queryset = Office.objects.all()


class OfficeCreateView(generics.CreateAPIView):
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer

    def perform_create(self, serializer):
        company_pk = self.kwargs.get('pk', None)
        if company_pk:
            company = Company.objects.get(pk=company_pk)
            serializer.save(company=company)
        else:
            serializer.save()


class OfficeUpdateView(generics.UpdateAPIView):
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer


class OfficeDeleteView(generics.DestroyAPIView):
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer
