# Generated by Django 4.1.5 on 2023-02-12 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RegModel',
            new_name='Staff',
        ),
    ]