import django_filters
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class FoodForm(ModelForm):
    class Meta:
        model = Food
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Please enter the food name'})
        self.fields['carbohydrate'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Please enter the total of carbohydrates'})
        self.fields['fats'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Please enter the total of fats'})
        self.fields['protein'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Please enter the total of proteins'})



class AddUserFood(ModelForm):
    class Meta:
        model = UserFood
        fields = "__all__"



class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Please enter your first name'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Please enter your last name'})
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Please enter your username'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Please enter your email'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Please enter your password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Please enter your password confirmation'})


class FoodFilter(django_filters.FilterSet):
    class Meta:
        model = Food
        fields = ['name', 'category', 'carbohydrate', 'fats', 'protein', 'calorie', 'quantity']



class AuthenticationNewForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control',
                                                     'placeholder': 'Please enter your username'})
        self.fields['password'].widget.attrs.update({'class': 'form-control',
                                                     'placeholder': 'Please enter your password'})

