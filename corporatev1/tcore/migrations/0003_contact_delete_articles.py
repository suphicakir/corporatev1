# Generated by Django 5.1.4 on 2024-12-29 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tcore', '0002_rename_body_articles_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=250)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Articles',
        ),
    ]
