# Generated by Django 3.2.5 on 2021-07-23 05:06

import datetime
from django.db import migrations
from django.utils.timezone import utc
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0019_alter_article_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=django_jalali.db.models.jDateTimeField(default=datetime.datetime(2021, 7, 23, 5, 6, 18, 776379, tzinfo=utc)),
        ),
    ]
