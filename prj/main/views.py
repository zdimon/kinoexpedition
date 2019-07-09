from django.shortcuts import render
from .models import Slider, Page, Gallery
def home(req):
    slider = Slider.objects.all()
    homepage = Page.objects.get(alias='home')
    schedulepage = Page.objects.get(alias='schedule')
    pages = Page.objects.all()
    gallery = Gallery.objects.all()
    cntx = {
        'slider': slider, 
        'homepage': homepage,
        'pages': pages,
        'schedulepage': schedulepage,
        'gallery': gallery
        }
    return render(req,'index.html', cntx)
