from django.contrib import admin
from django.urls import path
from django_app import views as api_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api_views.BikeList.as_view())
]
