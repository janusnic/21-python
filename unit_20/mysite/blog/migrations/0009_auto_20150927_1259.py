# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='categoty',
            new_name='category',
        ),
    ]
