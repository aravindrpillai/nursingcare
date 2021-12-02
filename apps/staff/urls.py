from django.urls import path
from .new_registration import views

urlpatterns = [
    path('apis/register/', views.StaffNewRegistration.as_view(), name='Register Staff API')
]