from django.urls import path
from . import views

urlpatterns = [
    path('create', views.EnUserViewSet.as_view()),
    path('list', views.CreateUserView.as_view())
]