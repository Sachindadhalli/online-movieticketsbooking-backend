# Generated by Django 4.0.4 on 2022-04-19 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_movie_detail_city_alter_theatre_city'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='theatre',
            name='name',
        ),
    ]