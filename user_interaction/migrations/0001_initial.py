# Generated by Django 3.0.3 on 2020-06-30 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_details',
            fields=[
                ('full_name', models.CharField(max_length=264)),
                ('user_name', models.CharField(max_length=264, primary_key=True, serialize=False, unique=True)),
                ('management_name', models.CharField(max_length=264)),
                ('contact_no', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('designation', models.CharField(max_length=264)),
                ('department', models.CharField(max_length=264)),
            ],
        ),
    ]