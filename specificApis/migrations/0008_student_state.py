# Generated by Django 3.1.1 on 2020-10-04 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specificApis', '0007_student_initpoints'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='state',
            field=models.IntegerField(default=0),
        ),
    ]