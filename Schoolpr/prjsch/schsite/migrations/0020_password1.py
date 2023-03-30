# Generated by Django 3.1.7 on 2021-04-10 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schsite', '0019_auto_20210407_2134'),
    ]

    operations = [
        migrations.CreateModel(
            name='Password1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=20, verbose_name='Пороль, минимум 8 символов')),
            ],
            options={
                'verbose_name': 'пороль',
                'verbose_name_plural': 'пороли',
                'abstract': False,
            },
        ),
    ]
