from django.urls import path, include
from . import views

urlpatterns = [
    path('register/',views.RegisterStaff.as_view(), name='Register Staff API')
]