# Generated by Django 3.1.2 on 2020-10-25 13:29

import ckeditor_uploader.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_task_completed'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('order', models.PositiveIntegerField(unique=True)),
                ('status', models.CharField(choices=[('A', 'Active'), ('D', 'Deleted')], default='A', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Diary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('diary_date', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[('A', 'Active'), ('D', 'Deleted')], default='A', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='ValueVisionMission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('value_text', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('vision_text', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('mission_text', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('puslish_date', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[('A', 'Active'), ('D', 'Deleted')], default='A', max_length=1)),
            ],
        ),
        migrations.RenameField(
            model_name='task',
            old_name='completed',
            new_name='closed',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='name',
            new_name='title',
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('blog_date', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[('A', 'Active'), ('D', 'Deleted')], default='A', max_length=1)),
                ('subject', models.ManyToManyField(blank=True, related_name='subject_blog', to='core.Subject')),
                ('subtopic', models.ManyToManyField(blank=True, related_name='subtopic_blog', to='core.Subtopic')),
            ],
        ),
    ]