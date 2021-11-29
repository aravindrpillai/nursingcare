from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('credential/',include('apps.core.urls')),
    path('user/',include('apps.users.urls')),
]