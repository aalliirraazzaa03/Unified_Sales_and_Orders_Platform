from django.urls import path
from .views import home, add_order

urlpatterns = [
    path('', home, name='app3-home'),
    path('add/', add_order, name='add-order'),
]
