# Generated by Django 5.0.7 on 2024-09-12 09:52

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_request'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
