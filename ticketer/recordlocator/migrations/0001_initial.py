# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('record_locator', models.CharField(serialize=False, max_length=10, primary_key=True)),
                ('timestamp_generated', models.DateTimeField(auto_now_add=True)),
                ('origin_zipcode', localflavor.us.models.USZipCodeField(max_length=10)),
            ],
        ),
    ]
