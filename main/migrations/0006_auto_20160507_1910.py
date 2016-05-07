# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20160507_1906'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='ciudad',
            field=models.ForeignKey(default=1, to='main.Ciudad'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='ciudad',
            field=models.ForeignKey(default=1, to='main.Ciudad'),
            preserve_default=False,
        ),
    ]
