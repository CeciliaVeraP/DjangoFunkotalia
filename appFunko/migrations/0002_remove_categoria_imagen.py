# Generated by Django 4.1.2 on 2023-07-01 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appFunko', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoria',
            name='imagen',
        ),
    ]