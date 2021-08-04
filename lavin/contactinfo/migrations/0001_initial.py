# Generated by Django 3.2.5 on 2021-08-03 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_Us',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='عنوان')),
                ('description', models.CharField(max_length=500, verbose_name='توضیحات')),
                ('phone', models.CharField(max_length=30, verbose_name='تلفن')),
                ('address', models.CharField(max_length=500, verbose_name='آدرس')),
                ('email', models.EmailField(max_length=50, verbose_name='ایمیل')),
                ('image', models.FileField(upload_to='contact-us', verbose_name='عکس')),
                ('fax', models.CharField(max_length=50, verbose_name='فکس')),
            ],
            options={
                'verbose_name': 'تنظیمات تماس با ما',
                'verbose_name_plural': 'ماژول تنظیمات',
            },
        ),
        migrations.CreateModel(
            name='ContactFormModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FullName', models.CharField(max_length=128, verbose_name='نام و نام خانوادگی')),
                ('Phone', models.CharField(max_length=128, verbose_name='تلفن')),
                ('Text', models.TextField(max_length=10000, verbose_name='متن پیام')),
            ],
            options={
                'verbose_name': 'اطلاعات کاربران',
                'verbose_name_plural': 'ماژول کاربران',
            },
        ),
    ]
