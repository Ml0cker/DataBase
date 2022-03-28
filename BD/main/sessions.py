from django import forms
from django.shortcuts import render,redirect
from django.conf import settings

class FormLogin(forms.Form):
    login = forms.CharField(max_length=30, label="Логин",required=True)
    password = forms.CharField(max_length=60, label="Пароль", widget=forms.PasswordInput,required=True)

def session(request):
    login = None
    formLogin = FormLogin()
    print(request.session._get_or_create_session_key())
    if request.method == 'GET':
        if 'action' in request.GET:
            action = request.GET.get('action')
            if action == 'logout':
                if request.session.has_key('login'):
                    request.session.flush()
                return redirect('session')

        if 'login' in request.session:
            login = request.session['login']
    elif request.method == 'POST':
        formLogin = FormLogin(request.POST)
        if formLogin.is_valid():
            login = formLogin.cleaned_data['login']
            password = formLogin.cleaned_data['password']
            if login.strip() == 'a' and password.strip() == 'a':
                request.session['login'] = login
            else:
                login = None
                'main/registration.html'

    return render(request, 'main/login.html', {
        'form': formLogin,
        'login': login,
    })
