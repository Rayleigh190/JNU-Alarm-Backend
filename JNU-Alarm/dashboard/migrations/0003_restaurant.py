# Generated by Django 5.0.1 on 2024-07-12 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_bannerad'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('road_address', models.CharField(max_length=50)),
                ('jibun_address', models.CharField(max_length=50)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('type', models.CharField(max_length=10)),
                ('naver_map_url', models.URLField()),
                ('is_available', models.BooleanField()),
            ],
        ),
    ]
