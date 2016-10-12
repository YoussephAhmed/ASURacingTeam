# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('rtMembers', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentImg',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('state', models.CharField(max_length=1000)),
                ('title', models.CharField(max_length=1000)),
                ('content', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='TicketComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='TicketImg',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.CharField(max_length=1000)),
                ('ticketid', models.ForeignKey(to='ticketSys.Ticket')),
            ],
        ),
        migrations.CreateModel(
            name='TicketMember',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('memberid', models.ForeignKey(to='rtMembers.RTMember')),
            ],
        ),
        migrations.AddField(
            model_name='ticketcomment',
            name='memberid',
            field=models.ForeignKey(to='ticketSys.TicketMember'),
        ),
        migrations.AddField(
            model_name='ticketcomment',
            name='ticketid',
            field=models.ForeignKey(to='ticketSys.Ticket'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='memberid',
            field=models.ForeignKey(to='ticketSys.TicketMember'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='userid',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='commentimg',
            name='commentid',
            field=models.ForeignKey(to='ticketSys.TicketComment'),
        ),
    ]
