# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketSys', '0008_auto_20161017_1323'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='member',
            new_name='ticketMember',
        ),
    ]
