# Generated by Django 3.2.5 on 2021-07-23 09:43

import datetime
from django.db import migrations
from django.utils.timezone import utc
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0024_alter_article_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=django_jalali.db.models.jDateTimeField(default=datetime.datetime(2021, 7, 23, 9, 43, 2, 16581, tzinfo=utc)),
        ),
    ]
