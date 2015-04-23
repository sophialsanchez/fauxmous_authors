# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('write', '0004_book_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_text',
            field=models.TextField(max_length=10000),
            preserve_default=True,
        ),
    ]
