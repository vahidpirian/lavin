# Generated by Django 3.2.5 on 2021-08-03 04:46

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Category', '0004_remove_category_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='توضیحات')),
                ('image', models.FileField(upload_to='Articles/', verbose_name='تصاویر')),
                ('categories', models.ManyToManyField(to='Category.Category', verbose_name='دسته بندی ها')),
            ],
            options={
                'verbose_name': 'مقاله',
                'verbose_name_plural': 'مقالات',
            },
        ),
    ]
