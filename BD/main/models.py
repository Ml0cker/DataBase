from django.db import models


class RegistrationData(models.Model):
    registrationDataID = models.AutoField(max_length=10, primary_key=True, name='ID регистрации')
    login = models.CharField(max_length=30, name='Логин', unique=True)
    password = models.CharField(max_length=60, name='Пароль')
    email = models.CharField(max_length=60, name='Email')
    sessionKey = models.CharField(max_length=60, default= ' ')

    def __str__(self):
        return self.Логин

    class Meta:
        verbose_name = "Регистрационные данные"
        verbose_name_plural = "Регистрационные даннные"


class User(models.Model):
    userID = models.OneToOneField(RegistrationData, on_delete=models.CASCADE, primary_key=True, )
    nickname = models.CharField(max_length=30, name='Никнейм', unique=True, null=True)
    name = models.CharField(max_length=30, name='Имя',null=True)
    surname = models.CharField(max_length=30, name='Фамилия',null=True)
    patronymic = models.CharField(max_length=30, name='Отчество',null=True)
    about = models.CharField(max_length=1000, name='Информация о пользователе', null=True)
    birthday = models.DateField(name='День рождения',null=True)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.Никнейм


class Friends(models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE,primary_key=True)
    friendID = models.ForeignKey(User, on_delete=models.CASCADE, related_name ="friendID")

    class Meta:
        verbose_name = "Друг"
        verbose_name_plural = "Друзья"

        unique_together =(('userID', 'friendID'))







class UserFhoto(models.Model):
    userPhotoID = models.AutoField(max_length=10, primary_key=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)

    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        verbose_name = "Фотография пользователя"
        verbose_name_plural = "Фотографии пользователя"








class Dialog(models.Model):
    dialogID = models.AutoField(max_length=10, primary_key=True)
    dialogName = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Диалог"
        verbose_name_plural = "Диалоги"

    def __str__(self):
        return self.dialogName




class UserDialog(models.Model):
    userID = models.ForeignKey(User, primary_key=True, on_delete=models.CASCADE)
    dialogID = models.ForeignKey(Dialog, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Диалог и пользователь"
        verbose_name_plural = "Диалоги и пользователи"





class Message(models.Model):
    messageID = models.AutoField(max_length=10, primary_key=True)
    messageText = models.CharField(max_length=1000)
    messageDateAndTime = models.DateTimeField(auto_now = True)

    dialogID = models.ForeignKey(Dialog, on_delete=models.CASCADE)
    userID = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"


class PhotoInMessage(models.Model):
    messagePhotoID = models.AutoField(max_length=10, primary_key=True)
    messagePhoto = models.ImageField(upload_to='message/%Y/%m/%d/', blank=True)

    messageID=models.ForeignKey(Message, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Фотография в сообщении"
        verbose_name_plural = "Фотографии в сообщениях"


