from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import *
from .models import *
from django.db.models import Q
from itertools import chain


def index(request):
    return render(request, 'base.html',)


def RegistrationPage(request):
    print(request.session._get_or_create_session_key())
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data.)

            form.save()
            print(form)
            return HttpResponseRedirect(reverse('loginPage',))
    else:
        form = RegistrationForm()
    return render(request, 'main/registration.html',
                  {'form': form})

def LoginPages(request):
    if request.method == 'POST':
        request = request.POST
        print(list(request.values())[1])
        print(list(request.values())[2])

        verificate = RegistrationData.objects.filter(Логин = list(request.values())[1], Пароль=list(request.values())[2])
        if verificate:
            return redirect('/main')


        return redirect('/main/login')
    else:
        form = LoginForm()
    return render(request, 'main/login.html',
                  {'form': form})

def LoginPage(request):
    loginForm = LoginForm()
    login = ' '
    sessionKey = request.session._get_or_create_session_key()
    print(sessionKey)
    if request.method == 'GET':
        if 'action' in request.GET:
            action = request.GET.get('action')
            if action == 'logout':
                registrationObject = RegistrationData.objects.get(sessionKey=sessionKey)
                print(registrationObject)
                registrationObject.sessionKey = ' '
                registrationObject.save()
                return render(request, 'main/login.html', {
                    'form': loginForm,
                    'login': login
                })
    if RegistrationData.objects.filter(sessionKey=sessionKey):
        login = sessionKey
    elif request.method == 'POST':
        loginForm = LoginForm(request.POST)
        if loginForm.is_valid():
            login = loginForm.cleaned_data['login']
            password = loginForm.cleaned_data['password']
            if RegistrationData.objects.filter(Логин = login.strip(), Пароль=password.strip()):
                print(RegistrationData.objects.get(Логин = login.strip(), Пароль=password.strip()))
                registrationObject = RegistrationData.objects.get(Логин = login.strip(), Пароль=password.strip())
                registrationObject.sessionKey = sessionKey
                registrationObject.save()
                return HttpResponseRedirect(reverse('userPage',))
            else:
                login = ' '




    return render(request, 'main/login.html', {
        'form': loginForm,
        'login': login
    })

def UserPage(request):
    sessionKey = request.session._get_or_create_session_key()
    form = UserForm()
    friends = []
    photos = []
    dialogs = []
    if RegistrationData.objects.filter(sessionKey=sessionKey):
        sessionKey = sessionKey
        objectRegistrationData = RegistrationData.objects.get(sessionKey=sessionKey)
        print(type(objectRegistrationData))
        #если создан
        if User.objects.filter(userID=objectRegistrationData):


            formTMP = User.objects.get(userID=objectRegistrationData)

            if UserDialog.objects.filter(userID=formTMP):
                print("ssas")
                dialogs = UserDialog.objects.filter(userID=formTMP)
                print(dialogs)
            if UserFhoto.objects.filter(userID=formTMP):
                photos = UserFhoto.objects.filter(userID=formTMP)
            print(formTMP)
            form = UserForm(instance=formTMP)

            if request.method == 'POST':
                form = UserForm(request.POST, instance=formTMP  )
                if form.is_valid():
                    form.save()
            if Friends.objects.filter(userID=formTMP):
                friends = Friends.objects.filter(userID=formTMP)


        elif request.method == 'POST':

            req = request.POST.dict()
            req['userID'] = objectRegistrationData
            print(req)
            form = UserForm(req)
            if form.is_valid():
                form.save()
                #return HttpResponseRedirect(reverse('index',))

        else:

            form = UserForm()

    return render(request, 'main/user.html',
                      {'form': form, 'friends':friends, 'photos':photos,'dialogs':dialogs})

def DialogPage(request, dialogID):
    sessionKey = request.session._get_or_create_session_key()
    listUserDialog = UserDialog.objects.filter(dialogID=dialogID)
    form = MessageForm()
    messages = []
    if RegistrationData.objects.filter(sessionKey=sessionKey):
        currectUser = User.objects.get(userID=RegistrationData.objects.get(sessionKey=sessionKey))
        otherUser = UserDialog.objects.get(~Q(userID = currectUser)).userID
        messages =  Message.objects.filter(dialogID = dialogID)
        photos = PhotoInMessage.objects.all()

        if request.method == 'POST':
            req = request.POST.dict()
            req['userID'] = currectUser
            req['dialogID'] = dialogID
            form = MessageForm(req)
            if form.is_valid():

                form.save()
                form = MessageForm()

    return render(request, 'main/dialog.html',
                  {'form': form, 'messages': messages,'photos':photos})