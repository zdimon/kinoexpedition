from django.contrib import admin
from .models import Page, Slider, Gallery
from image_cropping import ImageCroppingMixin

class PageAdmin(admin.ModelAdmin):
    list_display = ['title', 'alias']

admin.site.register(Page, PageAdmin)


class SliderAdmin(admin.ModelAdmin):
    list_display = ['photo', 'order']
    list_editable = ('order',)

admin.site.register(Slider, SliderAdmin)

class GalleryAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass

admin.site.register(Gallery, GalleryAdmin)
