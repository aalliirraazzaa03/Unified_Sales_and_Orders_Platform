from django.contrib import admin
from django.urls import path, include
from multi_app_project.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app1/', include('app1.urls')),
    path('app2/', include('app2.urls')),
    path('app3/', include('app3.urls')),
    path('', home, name='home'),  # root mapped to home
]
