# Generated by Django 3.2.14 on 2022-08-09 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('short_urls', '0018_alter_url_short_url_hash'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='password',
            field=models.CharField(max_length=64),
        ),
    ]