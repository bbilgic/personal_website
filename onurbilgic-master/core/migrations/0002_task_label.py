# Generated by Django 3.1.2 on 2020-10-12 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='label',
            field=models.ManyToManyField(blank=True, related_name='task_label', to='core.Label'),
        ),
    ]
