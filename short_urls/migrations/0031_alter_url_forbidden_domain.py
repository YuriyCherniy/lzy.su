# Generated by Django 3.2.14 on 2023-06-19 08:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('short_urls', '0030_auto_20230619_0741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='forbidden_domain',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='short_urls.forbiddendomain'),
        ),
    ]
