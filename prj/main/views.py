from django.shortcuts import render
from .models import Slider, Page, Gallery, Video
def home(req):
    slider = Slider.objects.all().order_by('order')
    #homepage = Page.objects.get(alias='home')
    #schedulepage = Page.objects.get(alias='schedule')
    video = Video.objects.all().order_by('order')
    pages = Page.objects.all().order_by('order')
    gallery = Gallery.objects.all()
    cntx = {
        'slider': slider, 
        #'homepage': homepage,
        'pages': pages,
        #'schedulepage': schedulepage,
        'gallery': gallery
        }
    return render(req,'index.html', cntx)
