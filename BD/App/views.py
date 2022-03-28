from django.http import HttpResponse
from django.shortcuts import render
from .forms import *


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def registrationPage(request):
    form = RegistrationForm()

    return render (request,'App/registration.html', {form:form})
