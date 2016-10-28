# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketSys', '0006_auto_20161017_1319'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticketmember',
            old_name='member',
            new_name='rtMember',
        ),
    ]
