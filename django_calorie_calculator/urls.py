from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('calorie.urls')),
    path('', include('user_calc.urls')),
    path('', include('users.urls')),
]
