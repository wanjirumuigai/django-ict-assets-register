# Generated by Django 5.0.7 on 2024-08-13 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='asset_tag',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
