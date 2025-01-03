# Generated by Django 5.1.4 on 2024-12-19 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bookapp', '0002_books_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='loginTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('password2', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('password2', models.CharField(max_length=200)),
            ],
        ),
    ]
