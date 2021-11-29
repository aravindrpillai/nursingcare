from django.urls import path, include
from . import views

urlpatterns = [
    path('api/', include('apps.core.api.urls'))
]