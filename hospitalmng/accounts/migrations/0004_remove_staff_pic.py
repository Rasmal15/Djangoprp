# Generated by Django 4.1.5 on 2023-02-14 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_staff_pic_alter_staff_email_alter_staff_experience_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='pic',
        ),
    ]
