# Generated by Django 4.1.4 on 2022-12-26 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorymodel',
            name='category_slug',
            field=models.SlugField(max_length=150, unique=True),
        ),
    ]
