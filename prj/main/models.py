from django.db import models
from django.utils.safestring import mark_safe
from tinymce.models import HTMLField
from image_cropping.fields import ImageRatioField, ImageCropField

# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length=250)
    content = HTMLField()
    alias =  models.CharField(max_length=250)
    def __str__(self):
        return self.title

class Slider(models.Model):
    title = models.CharField(max_length=250,null=True, blank=True)
    desc = HTMLField(null=True, blank=True)
    image = models.ImageField()

    def __str__(self):
        return mark_safe('<img width="100" src="/media/%s" />' % self.image)

from easy_thumbnails.files import get_thumbnailer

class Gallery(models.Model):
    title = models.CharField(max_length=250, null=True, blank=True)
    image = ImageCropField(blank=True, null=True, upload_to='uploaded_images')
    cropping = ImageRatioField('image', '150x150')

    @property
    def get_small_img(self):
        url = get_thumbnailer(self.image).get_thumbnail({
            'size': (150, 150),
            'box': self.cropping,
            'crop': True,
            'detail': True,
        }).url
        return url
    def __str__(self):
        thumbnail_url = get_thumbnailer(self.image).get_thumbnail({
            'size': (150, 150),
            'box': self.cropping,
            'crop': True,
            'detail': True,
        }).url
        return mark_safe('<img width="100" src="%s" />' % thumbnail_url)