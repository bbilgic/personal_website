# Generated by Django 3.1.2 on 2020-12-12 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('language', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='word',
            old_name='image',
            new_name='word_image',
        ),
    ]
