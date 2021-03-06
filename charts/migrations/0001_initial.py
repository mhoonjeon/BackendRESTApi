# Generated by Django 2.0.7 on 2018-08-07 11:30

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chart',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='charts', to='patients.Patient')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
