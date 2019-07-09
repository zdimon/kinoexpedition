from django.db import models
from django.utils.safestring import mark_safe
from tinymce.models import HTMLField


# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length=250)
    content = HTMLField()
    alias =  models.CharField(max_length=250)
    def __str__(self):
        return self.title

class Slider(models.Model):
    title = models.CharField(max_length=250)
    desc = HTMLField()
    image = models.ImageField()

    def __str__(self):
        return mark_safe('<img width="100" src="/media/%s" />' % self.image)

class Gallery(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField()
    def __str__(self):
        return mark_safe('<img width="100" src="/media/%s" />' % self.image)