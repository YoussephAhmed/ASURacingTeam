# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketSys', '0009_auto_20161017_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='ticketMember',
            field=models.ForeignKey(related_name='ticket', to='ticketSys.TicketMember'),
        ),
    ]
