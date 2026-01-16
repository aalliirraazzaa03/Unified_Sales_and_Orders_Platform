from django.urls import path
from .views import home, add_customer

urlpatterns = [
    path('', home, name='app2-home'),
    path('add/', add_customer, name='add-customer'),
]
