# Generated by Django 3.1.2 on 2020-10-13 05:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20201013_0821'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='note',
            name='note_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
