# Generated by Django 4.0.3 on 2022-10-23 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='short_url',
            field=models.URLField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
