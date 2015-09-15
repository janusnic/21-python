# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20150913_1117'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='status',
            field=models.CharField(default=b'0', max_length=1, choices=[(b'0', b'Dratf'), (b'1', b'Published'), (b'2', b'Not Published')]),
        ),
    ]
