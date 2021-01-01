# Generated by Django 3.1.2 on 2020-11-01 06:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_comment_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='pomodoro_count',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.CreateModel(
            name='Pomodoro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pomodoro_date', models.DateTimeField(blank=True, null=True)),
                ('pomodoro_count', models.IntegerField(blank=True, default=0, null=True)),
                ('task', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.task')),
            ],
        ),
    ]
