import datetime
import collections
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

from calorie.models import Food
from user_calc.models import FoodInADay, History


# def show_food_in_a_day(request):
#     foods = FoodInADay.objects.all()
#     foods_after_calculate = {}
#     foods_to_show = []
#
#     current_date = datetime.datetime.today().date()
#
#     for food in foods:
#         date = food.date
#         if date == current_date:
#             if food.name not in foods_after_calculate:
#                 foods_after_calculate[food.name] = []
#             foods_after_calculate[food.name].append(food)
#
#     total_calories = 0
#     for key, value in foods_after_calculate.items():
#         item = {
#             "name" : f"({len(value)}) {value[0].name}",
#             "carbohydrate" : value[0].carbohydrate * len(value),
#             "fats" : value[0].fats * len(value),
#             "protein" : value[0].protein * len(value),
#             "calorie" : value[0].calorie * len(value),
#             "quantity" : value[0].quantity * len(value),
#         }
#         foods_to_show.append(item)
#         total_calories += item["calorie"]
#
#         daily_calorie_goal = 2000
#         remaining_calories = daily_calorie_goal - total_calories_consumed
#
#     context = {
#         "total_calories" : total_calories,
#         "foods": foods_to_show
#     }
#
#     return render(request, 'user_calc/user_calc.html', context)

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

    total_calories_consumed = 0
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
        total_calories_consumed += item["calorie"]

    daily_calorie_goal = 2000
    remaining_calories = daily_calorie_goal - total_calories_consumed

    context = {
        "total_calories_consumed" : total_calories_consumed,
        "remaining_calories": remaining_calories,
        "daily_calorie_goal": daily_calorie_goal,
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

    sorted_dictionary = {key: value for key, value in sorted(full_history_with_date.items(), reverse=True)}
    context = {
        "full_history_with_date": sorted_dictionary,
    }

    return render(request, 'user_calc/history.html', context)


