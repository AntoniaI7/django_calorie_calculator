from django.db import models

from calorie.models import Category


# Create your models here.


class FoodInADay(models.Model):
    name = models.CharField(max_length=200)
    carbohydrate = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    fats = models.FloatField()
    protein = models.FloatField()
    calorie = models.FloatField(default=0, blank=True)
    quantity = models.IntegerField(default=1, null=True, blank=True)

    def __str__(self):
        return str(self.name)