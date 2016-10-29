# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketSys', '0012_auto_20161017_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticketimg',
            name='ticket',
            field=models.ForeignKey(to='ticketSys.Ticket', related_name='img'),
        ),
    ]
