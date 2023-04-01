from django.urls import path
from calorie import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    # path('', views.home, name='home_link'),
    # path('home/', views.home, name='home'),
    # path('home_page/', views.home_page, name='home_page'),

    path('user/', views.user_page, name='user_page'),
    path('food/', views.home, name='food_item'),
    path('createfooditem/', views.create_food_item, name='create_food_item'),
    # path('register/', views.register_page, name='register'),
    # path('login/', views.login_page, name='login'),
    # path('logout/', views.logout_user, name='logout'),
    path('add_food_item/', views.add_food_item, name='add_food_item'),
    path('reset_password/', auth_views.PasswordResetView.as_view(), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]