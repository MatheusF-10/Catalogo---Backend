# Generated by Django 3.2.5 on 2021-07-24 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0002_modulo_num_aulas'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='tipo',
            field=models.IntegerField(null=True),
        ),
    ]
