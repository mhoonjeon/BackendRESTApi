# Generated by Django 2.0.8 on 2018-11-23 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_auto_20181123_0556'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='follows_tag',
            field=models.ManyToManyField(related_name='followed_by', to='articles.Tag'),
        ),
    ]
