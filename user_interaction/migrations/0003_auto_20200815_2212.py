# Generated by Django 3.0.3 on 2020-08-15 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_interaction', '0002_studentmedicalreport'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentmedicalreport',
            old_name='account',
            new_name='account1',
        ),
    ]