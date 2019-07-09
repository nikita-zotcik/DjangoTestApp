from django.urls import path, include
from rest_framework.routers import DefaultRouter

import offices.api.views as api_views

router = DefaultRouter()

router.register(r"company", api_views.CompanyViewSet, basename="company")

urlpatterns = [
    path("", include(router.urls)),
    path("company/<int:pk>/offices", api_views.OfficeListAPIView.as_view(),
         name="company-offices"),
    path("company/<int:pk>/offices/create", api_views.OfficeCreateView.as_view(),
         name="offices-Office-create"),
    path("offices/delete/<int:pk>", api_views.OfficeDeleteView.as_view(),
         name="offices-delete"),
    path("offices/update/<int:pk>", api_views.OfficeUpdateView.as_view(),
         name="offices-update"),
    path("offices/create", api_views.OfficeCreateView.as_view(),
         name="offices-create"),
    path("offices/", api_views.OfficeListAPIView.as_view(),
         name="offices-list"),
]
