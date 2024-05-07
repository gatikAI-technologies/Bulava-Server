# Generated by Django 5.0.4 on 2024-05-06 11:46

import WeddingApp.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WeddingApp', '0008_coverimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coverimage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='covers/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])]),
        ),
    ]
