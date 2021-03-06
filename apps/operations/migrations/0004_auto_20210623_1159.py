# Generated by Django 2.2 on 2021-06-23 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0003_banner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='banner',
            options={'verbose_name': '轮播图', 'verbose_name_plural': '轮播图'},
        ),
        migrations.AlterField(
            model_name='banner',
            name='image',
            field=models.ImageField(max_length=200, upload_to='banner%Y/%m', verbose_name='轮播图'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='index',
            field=models.IntegerField(default=0, verbose_name='顺序'),
        ),
    ]
