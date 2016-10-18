# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rtMembers', '0006_auto_20161017_1252'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rtmember',
            old_name='userid',
            new_name='user',
        ),
    ]
