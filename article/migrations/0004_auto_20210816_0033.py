# Generated by Django 3.2.6 on 2021-08-15 21:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0003_article_articleimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sa', to=settings.AUTH_USER_MODEL, verbose_name='Yazar'),
        ),
        migrations.CreateModel(
            name='Commet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=20, verbose_name='Icerik')),
                ('content', models.TextField(max_length=100, verbose_name='Icerik')),
                ('createDate', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commet', to='article.article', verbose_name='commet')),
            ],
        ),
    ]