# Generated by Django 4.1.7 on 2023-03-08 21:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_user_avatar'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={},
        ),
        migrations.RemoveField(
            model_name='message',
            name='updated',
        ),
    ]
