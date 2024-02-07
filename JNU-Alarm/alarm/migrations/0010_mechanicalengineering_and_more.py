# Generated by Django 5.0.1 on 2024-02-07 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alarm', '0009_department_materials_engineering'),
    ]

    operations = [
        migrations.CreateModel(
            name='MechanicalEngineering',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.PositiveIntegerField()),
                ('title', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='department',
            name='mechanical_engineering',
            field=models.BooleanField(default=False),
        ),
    ]