# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distribuidoras', '0003_auto_20171005_1832'),
    ]

    operations = [
        migrations.AddField(
            model_name='distribuidora',
            name='cuit',
            field=models.BigIntegerField(default=0),
            preserve_default=False,
        ),
    ]