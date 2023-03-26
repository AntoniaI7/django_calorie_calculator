from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

from calorie.models import Food
from user_calc.models import FoodInADay


def show_food_in_a_day(request):
    foods = FoodInADay.objects.all()
    foods_after_calculate = {}
    foods_to_show = []
    for food in foods:
        if food.name not in foods_after_calculate:
            foods_after_calculate[food.name] = []
        foods_after_calculate[food.name].append(food)

    for key, value in foods_after_calculate.items():
        item = {
            "name" : f"({len(value)}) {value[0].name}",
            "carbohydrate" : value[0].carbohydrate * len(value),
            "fats" : value[0].fats * len(value),
            "protein" : value[0].protein * len(value),
            "calorie" : value[0].calorie * len(value),
            "quantity" : value[0].quantity * len(value),
        }
        foods_to_show.append(item)

    context = {
        "foods": foods_to_show
    }

    return render(request, 'user_calc/user_calc.html', context)