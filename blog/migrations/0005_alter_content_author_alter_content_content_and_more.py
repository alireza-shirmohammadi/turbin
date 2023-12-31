# Generated by Django 4.2.1 on 2023-06-15 08:36

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0004_alter_content_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL, verbose_name='نویسنده'),
        ),
        migrations.AlterField(
            model_name='content',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='توضیحات'),
        ),
        migrations.AlterField(
            model_name='content',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ارسال'),
        ),
        migrations.AlterField(
            model_name='content',
            name='short_desc',
            field=models.TextField(verbose_name='توضیحات کوتاه'),
        ),
        migrations.AlterField(
            model_name='content',
            name='slug',
            field=models.SlugField(max_length=200, unique=True, verbose_name='پیوند'),
        ),
        migrations.AlterField(
            model_name='content',
            name='status',
            field=models.IntegerField(choices=[(0, 'پیش نویس'), (1, 'منتشر شده')], default=0, verbose_name='وضعیت انتشار'),
        ),
        migrations.AlterField(
            model_name='content',
            name='tags',
            field=models.TextField(null=True, verbose_name='تگ ها'),
        ),
        migrations.AlterField(
            model_name='content',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='تصویر'),
        ),
        migrations.AlterField(
            model_name='content',
            name='title',
            field=models.CharField(max_length=200, unique=True, verbose_name='عنوان'),
        ),
        migrations.AlterField(
            model_name='content',
            name='updated_on',
            field=models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی'),
        ),
    ]
