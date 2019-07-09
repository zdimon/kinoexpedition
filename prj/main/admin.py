from django.contrib import admin
from .models import Page, Slider, Gallery

class PageAdmin(admin.ModelAdmin):
    list_display = ['title', 'alias']

admin.site.register(Page, PageAdmin)


class SliderAdmin(admin.ModelAdmin):
    pass

admin.site.register(Slider, SliderAdmin)

class GalleryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Gallery, GalleryAdmin)
