# Generated by Django 4.0.5 on 2022-06-09 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('short_urls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='pass_to_delete',
            field=models.IntegerField(default=''),
        ),
    ]
