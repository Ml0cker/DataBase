# Generated by Django 4.0 on 2021-12-29 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rename_id пользователя_user_userid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='friends',
            name='friendName',
            field=models.CharField(default=12312, max_length=30),
            preserve_default=False,
        ),
    ]
