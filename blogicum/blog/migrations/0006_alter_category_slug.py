# Generated by Django 3.2.16 on 2023-07-18 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20230717_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(help_text='Идентификатор страницы для URL;\n                            разрешены символы латиницы, цифры, дефис\n                            и подчёркивание.', unique=True, verbose_name='Идентификатор'),
        ),
    ]
