# Generated by Django 3.2.6 on 2021-08-15 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_alter_commet_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commet',
            name='author',
            field=models.CharField(max_length=20, verbose_name='Isim'),
        ),
    ]
