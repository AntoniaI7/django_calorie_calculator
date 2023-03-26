from django.urls import path
from user_calc import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('total_per_day/', views.show_food_in_a_day, name='total_per_day'),
    path('history/', views.generate_calorie_history, name='history'),
     # path('totalbreakfast/', views.home, name='total_breakfast'),
    # path('totallunch/', views.home, name='total_lunch'),
    # path('totalsnacks/', views.home, name='total_snacks'),
    # path('totaldinner/', views.home, name='total_dinner'),
    # path('totalcalorie/', views.home, name='total_calorie_today'),
]