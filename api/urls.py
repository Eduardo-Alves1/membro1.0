from django.urls import path
from .views import get_address_by_cep

urlpatterns = [
    path("get-address/<str:cep>/", get_address_by_cep, name="get_address_by_cep"),
]
