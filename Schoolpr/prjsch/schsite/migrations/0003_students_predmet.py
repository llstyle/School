# Generated by Django 3.1.7 on 2021-04-02 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schsite', '0002_items_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='predmet',
            field=models.ManyToManyField(to='schsite.Items', verbose_name='Предметы'),
        ),
    ]
