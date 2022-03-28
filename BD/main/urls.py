from django.urls import path
from .views import *
from .sessions import *

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/registration', views.RegistrationPage, name='registrationPage'),
    path('/login', views.LoginPage, name='loginPage'),
    path('/user', views.UserPage, name = 'userPage'),
    path('/dialog/<int:dialogID>', views.DialogPage, name = 'dialogPage'),

    path('/session', session, name='session'),
]