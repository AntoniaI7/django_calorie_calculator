import datetime

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

from calorie.models import Food
from user_calc.models import FoodInADay, History


def show_food_in_a_day(request):
    foods = FoodInADay.objects.all()
    foods_after_calculate = {}
    foods_to_show = []

    current_date = datetime.datetime.today().date()

    for food in foods:
        date = food.date
        if date == current_date:
            if food.name not in foods_after_calculate:
                foods_after_calculate[food.name] = []
            foods_after_calculate[food.name].append(food)

    total_calories = 0
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
        total_calories += item["calorie"]

    context = {
        "total_calories" : total_calories,
        "foods": foods_to_show
    }

    return render(request, 'user_calc/user_calc.html', context)


def generate_calorie_history(request):
    items = History.objects.all()
    full_history = []
    full_history_with_date= {}
    for itemFood in items:
        item = itemFood.foodInADayId
        if item.date not in full_history_with_date:
            full_history_with_date[item.date] = []
        full_history_with_date[item.date].append(item)

    context = {
        "full_history_with_date": full_history_with_date,
    }

    return render(request, 'user_calc/history.html', context)