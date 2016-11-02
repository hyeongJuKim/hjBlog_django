# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_image_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image_file',
            field=models.ImageField(upload_to='static_files/upload/%Y/%m/%d'),
        ),
    ]
