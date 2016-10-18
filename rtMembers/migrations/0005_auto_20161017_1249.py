# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rtMembers', '0004_auto_20161017_1248'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rtmember',
            old_name='userid',
            new_name='user',
        ),
    ]
