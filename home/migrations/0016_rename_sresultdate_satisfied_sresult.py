# Generated by Django 5.0 on 2024-01-19 06:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_satisfied'),
    ]

    operations = [
        migrations.RenameField(
            model_name='satisfied',
            old_name='sresultdate',
            new_name='sresult',
        ),
    ]
