# Generated by Django 5.0.4 on 2024-05-03 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Email')),
                ('full_name', models.CharField(max_length=255, verbose_name='Full Name')),
                ('phone', models.CharField(max_length=10, verbose_name='Phone')),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('role', models.CharField(default='User', max_length=10, verbose_name='Role')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
