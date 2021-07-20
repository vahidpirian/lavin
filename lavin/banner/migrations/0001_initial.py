# Generated by Django 3.2.5 on 2021-07-14 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان')),
                ('description', models.TextField(verbose_name='توضیحات')),
                ('image', models.FileField(blank=True, null=True, upload_to='banner/', verbose_name='تصویر')),
            ],
            options={
                'verbose_name': 'بنر',
                'verbose_name_plural': 'بنر',
            },
        ),
    ]
