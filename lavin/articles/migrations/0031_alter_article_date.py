# Generated by Django 3.2.5 on 2021-07-23 11:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0030_alter_article_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateTimeField(null=True, verbose_name=datetime.datetime(2021, 7, 23, 11, 5, 49, 448950, tzinfo=utc)),
        ),
    ]
