# Generated by Django 5.0.1 on 2024-07-14 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_restaurant'),
    ]

    operations = [
        migrations.AddField(
            model_name='bannerad',
            name='is_external_browser',
            field=models.BooleanField(default=False),
        ),
    ]
