# Generated by Django 2.0.7 on 2018-08-18 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0002_auto_20180818_0647'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='patient',
            options={'ordering': ['-id']},
        ),
    ]
