# Generated by Django 3.1.1 on 2020-09-23 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specificApis', '0005_auto_20200922_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=100),
        ),
    ]
