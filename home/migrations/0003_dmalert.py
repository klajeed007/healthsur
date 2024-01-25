# Generated by Django 5.0 on 2024-01-14 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_contactmessage_age_contactmessage_bmi_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DmAlert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('urine', models.IntegerField(default='')),
                ('tried', models.IntegerField(default='')),
                ('eat', models.IntegerField(default='')),
                ('wound', models.IntegerField(default='')),
                ('eye', models.IntegerField(default='')),
                ('dehy', models.IntegerField(default='')),
                ('hungry', models.IntegerField(default='')),
                ('pain', models.IntegerField(default='')),
                ('alertresult', models.IntegerField(default='0', null=True)),
            ],
        ),
    ]
