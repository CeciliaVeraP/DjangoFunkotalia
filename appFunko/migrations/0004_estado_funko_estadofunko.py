# Generated by Django 4.1.2 on 2023-07-01 22:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appFunko', '0003_funko_detalle'),
    ]

    operations = [
        migrations.CreateModel(
            name='estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estadoFunko', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='funko',
            name='estadoFunko',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='appFunko.estado'),
        ),
    ]