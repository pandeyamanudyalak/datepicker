# Generated by Django 4.1.1 on 2022-09-30 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calender_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calender',
            name='datefield',
            field=models.DateField(),
        ),
    ]
