# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketSys', '0011_auto_20161017_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentimg',
            name='comment',
            field=models.ForeignKey(related_name='img', to='ticketSys.TicketComment'),
        ),
        migrations.AlterField(
            model_name='ticketcomment',
            name='ticketMember',
            field=models.ForeignKey(related_name='comment', to='ticketSys.TicketMember'),
        ),
    ]
