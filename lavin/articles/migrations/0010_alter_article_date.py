# Generated by Django 3.2.5 on 2021-07-22 12:59

from django.db import migrations
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0009_alter_article_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=django_jalali.db.models.jDateField(),
        ),
    ]
