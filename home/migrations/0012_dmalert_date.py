# Generated by Django 5.0 on 2024-01-19 06:37

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_contactmessage_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='dmalert',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]