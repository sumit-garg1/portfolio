# Generated by Django 5.0.2 on 2024-08-07 03:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sumit', '0002_rename_email_message_enteremail_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='Enteremail',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='Entermessage',
            new_name='message',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='Entername',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='Enterphoneno',
            new_name='phoneno',
        ),
    ]
