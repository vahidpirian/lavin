# Generated by Django 3.2.5 on 2021-07-22 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banner', '0002_rename_banner_lavinbanner'),
    ]

    operations = [
        migrations.AddField(
            model_name='lavinbanner',
            name='links',
            field=models.CharField(max_length=500, null=True, verbose_name='لینک'),
        ),
    ]
