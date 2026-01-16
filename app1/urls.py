from django.urls import path
from .views import home, add_product

urlpatterns = [
    path('', home, name='app1-home'),
    path('add/', add_product, name='add-product'),
]
