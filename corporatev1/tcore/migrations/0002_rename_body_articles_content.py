# Generated by Django 5.1.4 on 2024-12-29 08:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tcore', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articles',
            old_name='body',
            new_name='content',
        ),
    ]