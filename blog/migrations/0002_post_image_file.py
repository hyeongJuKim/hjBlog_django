# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image_file',
            field=models.ImageField(upload_to='', default=datetime.datetime(2016, 10, 26, 15, 34, 35, 398165, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
