# Generated by Django 4.0 on 2022-01-21 01:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dialog',
            fields=[
                ('dialogID', models.AutoField(max_length=10, primary_key=True, serialize=False)),
                ('dialogName', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Диалог',
                'verbose_name_plural': 'Диалоги',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('messageID', models.AutoField(max_length=10, primary_key=True, serialize=False)),
                ('messageText', models.CharField(max_length=1000)),
                ('messageDateAndTime', models.DateTimeField(auto_now=True)),
                ('dialogID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.dialog')),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщения',
            },
        ),
        migrations.CreateModel(
            name='RegistrationData',
            fields=[
                ('ID регистрации', models.AutoField(max_length=10, primary_key=True, serialize=False)),
                ('Логин', models.CharField(max_length=30, unique=True)),
                ('Пароль', models.CharField(max_length=60)),
                ('Email', models.CharField(max_length=60)),
                ('sessionKey', models.CharField(default=' ', max_length=60)),
            ],
            options={
                'verbose_name': 'Регистрационные данные',
                'verbose_name_plural': 'Регистрационные даннные',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userID', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='main.registrationdata')),
                ('Никнейм', models.CharField(max_length=30, null=True, unique=True)),
                ('Имя', models.CharField(max_length=30, null=True)),
                ('Фамилия', models.CharField(max_length=30, null=True)),
                ('Отчество', models.CharField(max_length=30, null=True)),
                ('Информация о пользователе', models.CharField(max_length=1000, null=True)),
                ('День рождения', models.DateField(null=True)),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
        migrations.CreateModel(
            name='PhotoInMessage',
            fields=[
                ('messagePhotoID', models.AutoField(max_length=10, primary_key=True, serialize=False)),
                ('messagePhoto', models.ImageField(blank=True, upload_to='message/%Y/%m/%d/')),
                ('messageID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.message')),
            ],
            options={
                'verbose_name': 'Фотография в сообщении',
                'verbose_name_plural': 'Фотографии в сообщениях',
            },
        ),
        migrations.CreateModel(
            name='UserFhoto',
            fields=[
                ('userPhotoID', models.AutoField(max_length=10, primary_key=True, serialize=False)),
                ('photo', models.ImageField(blank=True, upload_to='users/%Y/%m/%d/')),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.user')),
            ],
            options={
                'verbose_name': 'Фотография пользователя',
                'verbose_name_plural': 'Фотографии пользователя',
            },
        ),
        migrations.AddField(
            model_name='message',
            name='userID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.user'),
        ),
        migrations.CreateModel(
            name='Friends',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('friendID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='friendID', to='main.user')),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.user')),
            ],
            options={
                'verbose_name': 'Друг',
                'verbose_name_plural': 'Друзья',
            },
        ),
        migrations.CreateModel(
            name='UserDialog',
            fields=[
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='main.user')),
                ('dialogID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.dialog')),
            ],
            options={
                'verbose_name': 'Диалог и пользователь',
                'verbose_name_plural': 'Диалоги и пользователи',
            },
        ),
    ]
