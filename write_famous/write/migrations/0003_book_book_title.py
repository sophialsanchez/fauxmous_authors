# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('write', '0002_book_book_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_title',
            field=models.CharField(default=' ', max_length=1000),
            preserve_default=False,
        ),
    ]
