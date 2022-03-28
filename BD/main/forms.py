from django import forms
from .models  import *



class RegistrationForm(forms.ModelForm):
    class Meta:
        model = RegistrationData
        fields = ['Логин', 'Пароль', 'Email']

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['messageText','userID','dialogID']
        widgets = {'userID': forms.HiddenInput(),'dialogID': forms.HiddenInput(), }
                    #['login', 'password', 'email']
        #widgets = {'login':forms.TextInput(attrs={'class': 'form-input'})}

class LoginForm(forms.Form):
    login = forms.CharField(max_length=30, label="Логин",required=True)
    password = forms.CharField(max_length=60, label="Пароль", widget=forms.PasswordInput,required=True)

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        #widget = forms.HiddenInput(),
        fields = ['userID','Никнейм', 'Имя', 'Фамилия', 'Отчество', 'Информация о пользователе', 'День рождения']
        #exclude = ['ID пользователя']
        widgets = {'userID':forms.HiddenInput(),}
