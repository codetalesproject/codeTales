# Generated by Django 3.2.5 on 2023-11-30 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codetales_app', '0004_listtrial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FullName', models.CharField(max_length=25)),
                ('Email', models.EmailField(max_length=254)),
                ('Password', models.CharField(max_length=20)),
            ],
        ),
    ]