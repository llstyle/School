# Generated by Django 3.1.7 on 2021-04-07 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schsite', '0016_kolurok_nomer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kolurok',
            name='nomer',
            field=models.PositiveIntegerField(blank=True, default='', verbose_name='Номер Урока'),
        ),
    ]
