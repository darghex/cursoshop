# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('main', '0002_auto_20160319_0712'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name='course',
            name='Chapter',
        ),
        migrations.AddField(
            model_name='chapter',
            name='course',
            field=models.ForeignKey(default=1, to='main.Course'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(upload_to='static/uploads/'),
        ),
    ]
