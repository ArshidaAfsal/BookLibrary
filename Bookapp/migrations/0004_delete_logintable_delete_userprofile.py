# Generated by Django 5.1.4 on 2024-12-19 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Bookapp', '0003_logintable_userprofile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='loginTable',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
