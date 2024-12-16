
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/',include('django.contrib.auth.urls')),
    path('',include('News.urls')),
    path('registration/',include('registration.urls')),
    path('ser/',include('api.urls')),
    path('ser/auth',include('rest_framework.urls')),


]
