# Generated by Django 3.0.3 on 2020-08-05 13:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_mysql.models
import user_interaction.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('joined_date', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(auto_now=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('management_name', models.CharField(max_length=254)),
                ('full_name', models.CharField(max_length=254, null=True)),
                ('contact_no', models.CharField(max_length=10)),
                ('department', models.CharField(max_length=254)),
                ('residential_status', models.CharField(max_length=254)),
                ('batch_year', models.CharField(default='Null', max_length=4)),
                ('entry_qrcode', models.ImageField(null=True, upload_to=user_interaction.models.qrcode_directory_path)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.CharField(max_length=40, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('temperature', models.DecimalField(decimal_places=1, max_digits=3)),
            ],
        ),
        migrations.CreateModel(
            name='StudentEntryDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entries', django_mysql.models.JSONField(default=list)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
