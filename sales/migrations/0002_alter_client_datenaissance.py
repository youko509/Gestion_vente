# Generated by Django 4.1.3 on 2023-10-02 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='dateNaissance',
            field=models.DateField(verbose_name='Date de Naissance'),
        ),
    ]
