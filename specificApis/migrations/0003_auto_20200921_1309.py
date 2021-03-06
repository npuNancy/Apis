# Generated by Django 3.1.1 on 2020-09-21 05:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('specificApis', '0002_auto_20200921_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classes',
            name='classNumber',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='specificApis.user'),
        ),
        migrations.AlterField(
            model_name='user',
            name='classNumber',
            field=models.CharField(db_index=True, max_length=20, unique=True),
        ),
    ]
