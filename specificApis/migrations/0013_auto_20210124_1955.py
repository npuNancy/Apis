# Generated by Django 3.1.1 on 2021-01-24 11:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('specificApis', '0012_remove_gradeadmin_types'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gradeadmin',
            name='grade',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='specificApis.grade', to_field='grade'),
        ),
    ]
