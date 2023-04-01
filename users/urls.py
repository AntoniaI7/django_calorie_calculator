from django.urls import path
from users import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register_page, name='register_link'),
    path('', auth_views.LoginView.as_view(template_name='users/login.html'), name='login_link'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout_link'),
]