# Generated by Django 5.0.1 on 2024-07-11 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shortcut',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('ios_image_name', models.CharField(max_length=20)),
                ('aos_image_name', models.CharField(max_length=20)),
                ('color_code', models.CharField(max_length=6)),
                ('link', models.URLField()),
                ('is_available', models.BooleanField()),
                ('is_webview', models.BooleanField()),
                ('is_modal', models.BooleanField()),
            ],
        ),
    ]
