# Generated by Django 5.0.1 on 2024-02-16 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alarm', '0002_homepost_homeset'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='device',
        ),
        migrations.AddField(
            model_name='notification',
            name='topic',
            field=models.TextField(default=3),
            preserve_default=False,
        ),
    ]