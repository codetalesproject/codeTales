# Generated by Django 4.2.5 on 2023-10-21 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codetales_app', '0003_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListTrial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Story', models.CharField(max_length=300)),
                ('Content', models.CharField(max_length=300)),
            ],
        ),
    ]
