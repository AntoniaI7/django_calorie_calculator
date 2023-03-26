# Generated by Django 4.1.7 on 2023-03-26 07:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calorie', '0003_remove_userfood_customer_remove_userfood_food_and_more'),
        ('user_calc', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodinaday',
            name='calorie',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='foodinaday',
            name='carbohydrate',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='foodinaday',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='calorie.category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='foodinaday',
            name='fats',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='foodinaday',
            name='protein',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='foodinaday',
            name='quantity',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]