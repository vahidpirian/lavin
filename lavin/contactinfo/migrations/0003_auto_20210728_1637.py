# Generated by Django 3.2.5 on 2021-07-28 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactinfo', '0002_contactformmodel'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactformmodel',
            options={'verbose_name': 'اطلاعات کاربران', 'verbose_name_plural': 'ماژول کاربران'},
        ),
        migrations.AlterField(
            model_name='contact_us',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='contactformmodel',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
