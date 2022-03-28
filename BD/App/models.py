from django.db import models


class User(models.Model):
    # userID = models.AutoField(max_length=10, primary_key=True, name='ID пользователя')
    nickname = models.CharField(max_length=30, name='Никнейм')
    name = models.CharField(max_length=30, name='Имя')
    surname = models.CharField(max_length=30, name='Фамилия')
    patronymic = models.CharField(max_length=30, name='Отчество')
    about = models.CharField(max_length=1000, name='Информация о пользователе')
    birthday = models.DateField(name='День рождения')

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):

        return self.name


class RegistrationData(models.Model):
    userID = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    # registrationDataID = models.AutoField(max_length=10, primary_key=True, name='ID регистрации')
    login = models.CharField(max_length=30, name='Логин')
    password = models.CharField(max_length=60, name='Пароль')
    email = models.CharField(max_length=60, name='Email')



    class Meta:
        verbose_name = "Регистрационные данные"
        verbose_name_plural = "Регистрационные даннные"

    def __str__(self):

        return self.name


class Friends(models.Model):
    userID = models.ForeignKey(User)
    friendID = models.ForeignKey(User,  related_name="friendID")


    class Meta:
        verbose_name = "Друг"
        verbose_name_plural = "Друзья"



class UserFhoto(models.Model):
    userPhotoID = models.AutoField(max_length=10, primary_key=True, name='ID фото пользователя')
    userPhotoPath = models.CharField(max_length=100, name='Путь к фотографии пользователя')

    class Meta:
        verbose_name = "Фотография пользователя"
        verbose_name_plural = "Фотографии пользователя"

    def __str__(self):
        return self.name





class Dialog(models.Model):
    dialogID = models.AutoField(max_length=10, primary_key=True, name='ID диалога')

    class Meta:
        verbose_name = "Диалог"
        verbose_name_plural = "Диалоги"

    def __str__(self):
        return self.name


class UserDialog(models.Model):
    userID = models.ForeignKey(User, primary_key=True, on_delete=models.CASCADE)
    dialogID = models.ForeignKey(Dialog, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Диалог и пользователь"
        verbose_name_plural = "Диалоги и пользователи"

    def __str__(self):
        return self.name


class Message(models.Model):
    messageID = models.AutoField(max_length=10, primary_key=True, name='ID сообщения')
    messageText = models.CharField(max_length=1000, name='Текст сообщения')
    messageDateAndTime = models.DateTimeField( name='Дата и время сообщения')

    dialogID = models.ForeignKey(Dialog, on_delete=models.CASCADE)
    userID = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"

    def __str__(self):
        return self.name

class PhotoInMessage(models.Model):
    messagePhotoID = models.AutoField(max_length=10, primary_key=True, name='ID фотографии в сообшениях')
    messagePhotoPath = models.CharField(max_length=101, name='Путь к фотографии в сообщении')

    messageID=models.ForeignKey(Message, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Фотография в сообщении"
        verbose_name_plural = "Фотографии в сообщениях"

    def __str__(self):
        return self.name

