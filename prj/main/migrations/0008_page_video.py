# Generated by Django 2.2.3 on 2019-07-11 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20190711_0732'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]