# Generated by Django 2.0.7 on 2018-09-07 13:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_article_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='owner',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
