# Generated by Django 4.0.5 on 2022-06-12 22:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('short_urls', '0007_rename_salt_url_clck'),
    ]

    operations = [
        migrations.RenameField(
            model_name='url',
            old_name='clck',
            new_name='click',
        ),
    ]
