# Generated by Django 2.2a1 on 2019-02-02 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nehapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='songs',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
    ]
