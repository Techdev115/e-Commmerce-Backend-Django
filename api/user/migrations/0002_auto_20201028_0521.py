# Generated by Django 3.1.2 on 2020-10-28 05:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='Gender',
            new_name='gender',
        ),
    ]
