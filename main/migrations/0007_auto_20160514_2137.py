# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20160507_1910'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='foto',
            field=models.ImageField(default='', upload_to='photos/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacher',
            name='profile',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='foto',
            field=models.ImageField(default='', upload_to='photos/'),
            preserve_default=False,
        ),
    ]
