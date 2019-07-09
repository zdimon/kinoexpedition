from django.core.management.base import BaseCommand, CommandError
from main.models import Page, Slider, Gallery
from prj.settings import BASE_DIR
import os
from django.core.files import File

class Command(BaseCommand):
    def handle(self, *args, **options):
        print('Start loading...')
        Page.objects.all().delete()
        Slider.objects.all().delete()
        Gallery.objects.all().delete()
        # главная
        path = os.path.join(BASE_DIR,'..','data','index.txt')
        with open(path,'r') as f:
            txt = f.read()
        print(txt)
        p = Page()
        p.title = 'О нас'
        p.content = txt
        p.alias = 'home'
        p.save()

        # расписание

        path = os.path.join(BASE_DIR,'..','data','schedule.txt')
        with open(path,'r') as f:
            txt = f.read()
        print(txt)
        p = Page()
        p.title = 'Расписание'
        p.content = txt
        p.alias = 'schedule'
        p.save()

        # импорт картинок слайдера
        for i in range(1,5):
            img = '%s.jpg' % i
            img_abspath = os.path.join(BASE_DIR,'..','data',img)
            print('Importing... %s' % img_abspath)
            s = Slider()
            s.title = img
            s.desc = 'Description of %s' % img
            s.save()
            with open(img_abspath, 'rb') as doc_file:
                s.image.save(img, File(doc_file), save=True)

        # импорт галереи
        for i in range(1,22):
            img = '%s.jpg' % i
            img_abspath = os.path.join(BASE_DIR,'..','data','gallery',img)
            g = Gallery()
            g.title = img
            g.save()
            with open(img_abspath, 'rb') as doc_file:
                g.image.save(img, File(doc_file), save=True)
        