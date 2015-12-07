# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='address',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='location',
            name='hours',
            field=models.TextField(null=True, blank=True),
        ),
    ]
