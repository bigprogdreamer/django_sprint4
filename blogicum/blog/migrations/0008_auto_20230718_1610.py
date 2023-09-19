# Generated by Django 3.2.16 on 2023-07-18 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20230718_1109'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='location',
            options={'verbose_name': 'местоположение', 'verbose_name_plural': 'Местоположения'},
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(help_text='Идентификатор страницы для URL;\n                            разрешены символы латиницы, цифры,\n                            дефис и подчёркивание.', unique=True, verbose_name='Идентификатор'),
        ),
    ]
