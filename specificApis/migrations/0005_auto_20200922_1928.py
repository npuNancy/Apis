# Generated by Django 3.1.1 on 2020-09-22 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specificApis', '0004_auto_20200921_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdata',
            name='duration',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='points',
            field=models.DecimalField(decimal_places=5, default=0, max_digits=10),
        ),
    ]