# Generated by Django 4.1.7 on 2023-03-26 10:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_calc', '0002_foodinaday_calorie_foodinaday_carbohydrate_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodinaday',
            name='date',
            field=models.DateField(default=datetime.datetime.today),
        ),
    ]
