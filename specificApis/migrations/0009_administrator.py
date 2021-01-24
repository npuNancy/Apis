# Generated by Django 3.1.1 on 2021-01-17 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specificApis', '0008_student_state'),
    ]

    operations = [
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(db_index=True, max_length=20, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('types', models.CharField(max_length=20)),
            ],
        ),
    ]
