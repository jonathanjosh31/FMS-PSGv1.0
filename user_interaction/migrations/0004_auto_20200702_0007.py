# Generated by Django 3.0.3 on 2020-07-01 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_interaction', '0003_auto_20200630_1947'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_detail',
            old_name='department',
            new_name='residential_status',
        ),
        migrations.RenameField(
            model_name='user_detail',
            old_name='user_name',
            new_name='roll_no',
        ),
    ]