# Generated by Django 4.2.3 on 2023-08-15 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_advertisment', '0004_advertisement_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='advertisements/', verbose_name='Изображение'),
        ),
    ]
