# Generated by Django 2.0.7 on 2018-09-07 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_article_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='owner',
        ),
    ]
