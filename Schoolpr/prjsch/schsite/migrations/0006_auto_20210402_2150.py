# Generated by Django 3.1.7 on 2021-04-02 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schsite', '0005_auto_20210402_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='predmet',
            field=models.ManyToManyField(blank=True, to='schsite.Students', verbose_name='Предметы'),
        ),
    ]
