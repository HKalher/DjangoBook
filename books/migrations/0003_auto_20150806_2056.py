# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_isbn'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='edition',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='ISBN',
            field=models.CharField(max_length=20),
        ),
    ]
