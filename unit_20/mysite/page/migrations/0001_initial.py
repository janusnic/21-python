# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import page.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.IntegerField(default=1, choices=[(1, b'Published'), (2, b'Hidden')])),
                ('title', models.CharField(max_length=32)),
                ('slug', models.SlugField(unique=True)),
                ('content', models.TextField()),
                ('featured_image', models.ImageField(max_length=1024, null=True, upload_to=page.models.get_page_file_name, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.IntegerField(default=1, choices=[(1, b'Published'), (2, b'Hidden')])),
                ('title', models.CharField(max_length=32)),
                ('description', models.TextField(null=True, blank=True)),
                ('image', models.ImageField(max_length=1024, null=True, upload_to=page.models.get_page_file_name, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.IntegerField(default=1, choices=[(1, b'Published'), (2, b'Hidden')])),
                ('title', models.CharField(max_length=32)),
                ('description', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='slide',
            name='related_slider',
            field=models.ForeignKey(to='page.Slider'),
        ),
        migrations.AddField(
            model_name='page',
            name='related_slider',
            field=models.ForeignKey(blank=True, to='page.Slider', null=True),
        ),
    ]
