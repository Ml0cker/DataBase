# Generated by Django 4.0 on 2021-12-29 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_rename_дата и время сообщения_message_messagedateandtime_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photoinmessage',
            name='messagePhotoPath',
        ),
        migrations.AddField(
            model_name='photoinmessage',
            name='messagePhoto',
            field=models.ImageField(blank=True, upload_to='message/%Y/%m/%d/'),
        ),
    ]
