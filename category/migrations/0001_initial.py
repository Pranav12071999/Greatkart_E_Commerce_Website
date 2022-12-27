# Generated by Django 4.1.4 on 2022-12-26 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=150, unique=True)),
                ('category_slug', models.CharField(max_length=150, unique=True)),
                ('category_description', models.TextField(blank=True)),
                ('category_image', models.ImageField(blank=True, upload_to='photoes/categories/')),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
    ]
