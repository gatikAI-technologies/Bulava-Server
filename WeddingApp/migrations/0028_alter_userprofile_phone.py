# Generated by Django 5.0.6 on 2024-07-24 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WeddingApp', '0027_alter_userprofile_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(blank=True, max_length=10, null=True, unique=True, verbose_name='Phone'),
        ),
    ]
