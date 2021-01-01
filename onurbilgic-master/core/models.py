from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.utils.html import mark_safe,escape
from django.urls import reverse
# Create your models here.
from io import BytesIO
from PIL import Image
from django.core.files import File

from gdstorage.storage import GoogleDriveStorage

gd_storage = GoogleDriveStorage()
User = get_user_model()

class HomePage(models.Model):
    ACTIVE = 'A'
    DELETED = 'D'
    Status = (
        (ACTIVE, 'Active'),
        (DELETED, 'Deleted'),
    )
    name=models.CharField(max_length=256)
    text=RichTextUploadingField(null=True, blank=True)
    order= models.PositiveIntegerField(unique=True)
    status = models.CharField(max_length=1, choices=Status, default=ACTIVE)

    def __str__(self):
        return self.name

    def text_tag(self):
        return mark_safe(self.text)

    text_tag.short_description = 'Home Text'
    text_tag.allow_tags = True

class AboutPage(models.Model):
    ACTIVE = 'A'
    DELETED = 'D'
    Status = (
        (ACTIVE, 'Active'),
        (DELETED, 'Deleted'),
    )
    name=models.CharField(max_length=256)
    text=RichTextUploadingField(null=True, blank=True)
    order= models.PositiveIntegerField(unique=True)
    status = models.CharField(max_length=1, choices=Status, default=ACTIVE)

    def __str__(self):
        return self.name

    def text_tag(self):
        return mark_safe(self.text)

    text_tag.short_description = 'About Text'
    text_tag.allow_tags = True


class Label(models.Model):
    ACTIVE = 'A'
    DELETED = 'D'
    Status = (
        (ACTIVE, 'Active'),
        (DELETED, 'Deleted'),
    )
    name = models.CharField(max_length=255)
    color_code = models.CharField(max_length=16,null=True,blank=True)
    status = models.CharField(max_length=1, choices=Status, default=ACTIVE)

    def __str__(self):
        return self.name


class Subject(models.Model):
    ACTIVE = 'A'
    DELETED = 'D'
    Status = (
        (ACTIVE, 'Active'),
        (DELETED, 'Deleted'),
    )
    name = models.CharField(max_length=128)
    description = RichTextUploadingField(null=True, blank=True)
    label = models.ManyToManyField(Label, related_name='subject_label', blank=True)
    status = models.CharField(max_length=1, choices=Status, default=ACTIVE)

    def __str__(self):
        return self.name

class Subtopic(models.Model):
    ACTIVE = 'A'
    DELETED = 'D'
    Status = (
        (ACTIVE, 'Active'),
        (DELETED, 'Deleted'),
    )
    name = models.CharField(max_length=128)
    description = RichTextUploadingField(null=True, blank=True)
    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING, blank=True, null=True)
    label = models.ManyToManyField(Label, related_name='subtopic_label', blank=True)
    status = models.CharField(max_length=1, choices=Status, default=ACTIVE)

    def __str__(self):
        return self.name

class Goal(models.Model):
    ACTIVE = 'A'
    DELETED = 'D'
    Status = (
        (ACTIVE, 'Active'),
        (DELETED, 'Deleted'),
    )
    name = models.CharField(max_length=128)
    description = RichTextUploadingField(null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    due_date= models.DateTimeField(blank=True, null=True)
    subject = models.ManyToManyField(Subject, related_name='subject_goal', blank=True)
    subtopic = models.ManyToManyField(Subtopic, related_name='subtopic_goal', blank=True)
    label = models.ManyToManyField(Label, related_name='label_goal', blank=True)
    status = models.CharField(max_length=1, choices=Status, default=ACTIVE)

    def __str__(self):
        return self.name


class Task(models.Model):
    ACTIVE = 'A'
    DELETED = 'D'
    Status = (
        (ACTIVE, 'Active'),
        (DELETED, 'Deleted'),
    )
    title = models.CharField(max_length=128)
    description = RichTextUploadingField(null=True, blank=True)
    subject = models.ManyToManyField(Subject, related_name='subject_task', blank=True)
    subtopic = models.ManyToManyField(Subtopic, related_name='subtopic_task', blank=True)
    goal = models.ManyToManyField(Goal, related_name='goal_task', blank=True)
    label = models.ManyToManyField(Label, related_name='task_label', blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    action_date = models.DateTimeField(blank=True, null=True)
    due_date = models.DateTimeField(blank=True, null=True)
    closed=models.BooleanField(default=False)
    note=models.ManyToManyField('core.Note', related_name='task_note', blank=True)
    points=models.IntegerField(null=True,blank=True)
    pomodoro_count=models.IntegerField(default=0,null=True,blank=True)
    status = models.CharField(max_length=1, choices=Status, default=ACTIVE)

    def __str__(self):
        return self.title

    def description_tag(self):
        return mark_safe(self.description)

    description_tag.short_description = 'Description'
    description_tag.allow_tags = True



class Pomodoro(models.Model):
    task=models.ForeignKey(Task,on_delete=models.DO_NOTHING,null=True,blank=True)
    pomodoro_date=models.DateTimeField(blank=True, null=True)
    pomodoro_count=models.IntegerField(default=0,null=True,blank=True)

    def __str__(self):
        return str(self.task)+' - '+str(self.pomodoro_date)


class Note(models.Model):
    ACTIVE = 'A'
    DELETED = 'D'
    Status = (
        (ACTIVE, 'Active'),
        (DELETED, 'Deleted'),
    )
    title = models.CharField(max_length=200,null=True, blank=True)
    text = RichTextUploadingField(null=True, blank=True)
    subject = models.ManyToManyField(Subject, related_name='subject_note', blank=True)
    subtopic = models.ManyToManyField(Subtopic, related_name='subtopic_note', blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    note_date = models.DateTimeField(blank=True, null=True)
    goal = models.ManyToManyField(Goal, related_name='goal_note', blank=True)
    task = models.ManyToManyField(Task, related_name='task_note', blank=True)
    status = models.CharField(max_length=1, choices=Status, default=ACTIVE)

    def __str__(self):
        if self.title:
            return self.title
        elif self.text:
            return  str(self.text)[:50]
        else:
            return 'No title'


class Blog(models.Model):
    ACTIVE = 'A'
    DELETED = 'D'
    Status = (
        (ACTIVE, 'Active'),
        (DELETED, 'Deleted'),
    )
    title = models.CharField(max_length=200,null=True, blank=True)
    text = RichTextUploadingField(null=True, blank=True)
    subject = models.ManyToManyField(Subject, related_name='subject_blog', blank=True)
    subtopic = models.ManyToManyField(Subtopic, related_name='subtopic_blog', blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    blog_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=1, choices=Status, default=ACTIVE)

    def __str__(self):
        if self.title:
            return self.title
        elif self.text:
            return  str(self.text)[:50]
        else:
            return 'No title'

class ValueVisionMission(models.Model):
    ACTIVE = 'A'
    DELETED = 'D'
    Status = (
        (ACTIVE, 'Active'),
        (DELETED, 'Deleted'),
    )
    title = models.CharField(max_length=200,null=True, blank=True)
    value_text = RichTextUploadingField(null=True, blank=True)
    vision_text = RichTextUploadingField(null=True, blank=True)
    mission_text = RichTextUploadingField(null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    publish_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=1, choices=Status, default=ACTIVE)

    def __str__(self):
        if self.title:
            return self.title
        elif self.text:
            return  str(self.text)[:50]
        else:
            return 'No title'


class Diary(models.Model):
    ACTIVE = 'A'
    DELETED = 'D'
    Status = (
        (ACTIVE, 'Active'),
        (DELETED, 'Deleted'),
    )
    title = models.CharField(max_length=200,null=True, blank=True)
    text = RichTextUploadingField(null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    diary_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=1, choices=Status, default=ACTIVE)

    def __str__(self):
        if self.title:
            return self.title
        elif self.text:
            return  str(self.text)[:50]
        else:
            return 'No title'



class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    text = RichTextUploadingField(null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    def get_absolute_url(self):
        return reverse("core:post_detail",kwargs={'pk':self.pk})


    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('core.Post', related_name='comments',on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = RichTextUploadingField(null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse("core:post_detail")

    def __str__(self):
        return mark_safe( self.text)

