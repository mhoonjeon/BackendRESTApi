# Generated by Django 2.0.8 on 2018-11-13 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0005_auto_20181113_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]
