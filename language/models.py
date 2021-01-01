from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.html import escape
from django.utils.safestring import mark_safe
from gdstorage.storage import GoogleDriveStorage


from io import BytesIO
from PIL import Image
from django.core.files import File
from math import floor

def compress(image):
    im = Image.open(image)
    if im.mode in ("RGBA", "P"):
        im = im.convert("RGB")
    width, height = im.size
    if width > 2000:
        ratio = height / width
        newheight = floor(ratio * 2000)
        im = im.resize((2000, newheight), Image.ANTIALIAS)
    im_io = BytesIO()
    im.save(im_io, 'JPEG', quality=60, dpi=[300, 300], )
    new_image = File(im_io, name=image.name)
    return new_image

gd_storage = GoogleDriveStorage()
User = get_user_model()


class Language(models.Model):
    ACTIVE = 'A'
    DELETED = 'D'
    Status = (
        (ACTIVE, 'Active'),
        (DELETED, 'Deleted'),
    )
    name = models.CharField(max_length=200,null=True, blank=True)
    definition = RichTextUploadingField(null=True, blank=True)
    family = models.CharField(max_length=200,null=True, blank=True)
    code= models.CharField(max_length=10,null=True, blank=True)
    status = models.CharField(max_length=1, choices=Status, default=ACTIVE)
    def __str__(self):
       return  self.name


class Category(models.Model):
    ACTIVE = 'A'
    DELETED = 'D'
    Status = (
        (ACTIVE, 'Active'),
        (DELETED, 'Deleted'),
    )
    name = models.CharField(max_length=200,null=True, blank=True)
    definition = RichTextUploadingField(null=True, blank=True)
    status = models.CharField(max_length=1, choices=Status, default=ACTIVE)

    def __str__(self):
       return  self.name


class Word(models.Model):
    ACTIVE = 'A'
    DELETED = 'D'
    Status = (
        (ACTIVE, 'Active'),
        (DELETED, 'Deleted'),
    )
    name = models.CharField(max_length=128)
    definiton = models.TextField(null=True, blank=True  )
    word_image= models.ImageField(upload_to='images', null=True, blank=True, storage=gd_storage)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    language=models.ForeignKey(Language,on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=1, choices=Status, default=ACTIVE)

    def __str__(self):
         return self.name

    def save(self, *args, **kwargs):
        try :
            if self.word_image.file:
                new_image = compress(self.word_image)
                self.word_image = new_image
                super().save(*args, **kwargs)
        except:
               super().save(*args, **kwargs)


    def image_tag(self):
        if self.word_image:
            return mark_safe(u'<img src="%s" width="200" height="200" />' % escape(self.word_image.url))
        else:
            return mark_safe(u'<p></p>')
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True