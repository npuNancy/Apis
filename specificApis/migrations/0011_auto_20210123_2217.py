# Generated by Django 3.1.1 on 2021-01-23 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('specificApis', '0010_grade_gradeadmin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='administrator',
            name='types',
        ),
        migrations.RemoveField(
            model_name='grade',
            name='gradeAdmin',
        ),
        migrations.CreateModel(
            name='GradeAdmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(db_index=True, max_length=20, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('types', models.CharField(max_length=20)),
                ('grade', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='specificApis.grade', to_field='grade')),
            ],
        ),
    ]
