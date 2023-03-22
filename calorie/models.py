from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.name)


class Category(models.Model):
    options = (
        ('breakfast', 'breakfast'),
        ('lunch', 'lunch'),
        ('dinner', 'dinner'),
        ('snacks', 'snacks'),
    )
    name = models.CharField(max_length=50, choices=options)

    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=200)
    # category = models.ManyToManyField(Category)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    carbohydrate = models.FloatField()
    fats = models.FloatField()
    protein = models.FloatField()
    calorie = models.FloatField(default=0, blank=True)
    quantity = models.IntegerField(default=1, null=True, blank=True)

    def __str__(self):
        return str(self.name)


class UserFood(models.Model):
    customer = models.ForeignKey(Customer, blank=True, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)