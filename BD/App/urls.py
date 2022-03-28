from django.urls import path
from .views import *

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registration', views.registrationPage, name='registrationPage'),
]