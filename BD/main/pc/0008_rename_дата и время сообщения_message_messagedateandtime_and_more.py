# Generated by Django 4.0 on 2021-12-29 23:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_rename_id диалога_dialog_dialogid_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='Дата и время сообщения',
            new_name='messageDateAndTime',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='ID сообщения',
            new_name='messageID',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='Текст сообщения',
            new_name='messageText',
        ),
        migrations.RenameField(
            model_name='photoinmessage',
            old_name='ID фотографии в сообшениях',
            new_name='messagePhotoID',
        ),
        migrations.RenameField(
            model_name='photoinmessage',
            old_name='Путь к фотографии в сообщении',
            new_name='messagePhotoPath',
        ),
    ]
