# Generated by Django 3.2.6 on 2021-08-15 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20210815_0046'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='articleImage',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Resim Ekle'),
        ),
    ]
