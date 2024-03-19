# Generated by Django 4.2.6 on 2024-03-17 16:13

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_delete_mags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Research',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='ResearchImages', verbose_name='عکس مطلب')),
                ('header', models.CharField(max_length=100, verbose_name='عنوان مطلب')),
                ('slug', models.SlugField(blank=True, max_length=150, null=True, unique=True, verbose_name='نام آدرس بار')),
                ('preview', models.CharField(max_length=200, verbose_name='پیش نمایش')),
                ('body', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='متن اصلی')),
            ],
            options={
                'verbose_name': 'مطالب منتشر شده  ',
                'verbose_name_plural': 'مطالب',
            },
        ),
    ]