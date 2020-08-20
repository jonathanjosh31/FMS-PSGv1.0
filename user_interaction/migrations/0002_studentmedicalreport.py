# Generated by Django 3.0.3 on 2020-08-15 15:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('user_interaction', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentMedicalReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medical_reports', django_mysql.models.JSONField(default=list)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
