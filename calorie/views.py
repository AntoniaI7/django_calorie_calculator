from django.shortcuts import render
from django.template import context
from django.urls import reverse_lazy
from django.views.generic import CreateView

from user_calc.models import FoodInADay, History
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import *
from django.contrib.auth.models import Group



def home(request):
    return HttpResponse('<h1>Calorie Calculator</h1>')

def home_page(request):
    return render(request, 'calorie/home_page.html')


# @login_required(login_url='login')
# @admin_only
def home(request):
    food = Food.objects.all()
    lunch = []
    snacks = []
    breakfast = []
    dinner = []
    customers = []
    for f in food:
        if f.category.name == "snacks":
            snacks.append(f)
        elif f.category.name == "lunch":
            lunch.append(f)
        elif f.category.name == "dinner":
            dinner.append(f)
        elif f.category.name == "breakfast":
            breakfast.append(f)
        else:
            customers.append(f)


    context = {
        'breakfast': breakfast,
        'lunch': lunch,
        'dinner': dinner,
        'snacks': snacks,
        'customers': customers,
    }
    # lunch = Category.objects.filter(name='lunch')[0].fooditem_set.all()
    # dinner = Category.objects.filter(name='dinner')[0].fooditem_set.all()
    # snacks = Category.objects.filter(name='snacks')[0].fooditem_set.all()
    # customers = Customer.objects.all()
    # context = {'breakfast': breakfast,
    #            'lunch': lunch,
    #            'dinner': dinner,
    #            'snacks': snacks,
    #            'customers': customers,
    #            }

    # in felul de mai jos, putem identifica ce buton a fost apasat
    # folosind doar numele lui ca si identificator.
    # toate apasarile de butoane se afla in lista request.POST

    if 'addToMyListButton' in request.POST:
        primaryKeyOfFood = request.POST['addToMyListButton']
        itemComplet = Food.objects.filter(pk=primaryKeyOfFood)
        for item in itemComplet:
            instance = FoodInADay.objects.create(
                name=item.name,
                category = item.category,
                carbohydrate = item.carbohydrate,
                fats = item.fats,
                protein = item.protein,
                calorie = item.calorie,
                quantity = item.quantity,
            )
            History.objects.create(foodInADayId = instance)

    return render(request, 'calorie/fooditem.html', context)


# @login_required(login_url='login')
# @allowed_users(allowed_roles=['admin'])
def fooditem(request):
    food = Food.objects.all()
    lunch = []
    snacks = []
    breakfast = []
    dinner = []
    customers = []
    for f in food:
        if f.category.name == "snacks":
            snacks.append(f)
        elif f.category.name == "lunch":
            lunch.append(f)
        elif f.category.name == "dinner":
            dinner.append(f)
        elif f.category.name == "breakfast":
            breakfast.append(f)
        else:
            customers.append(f)

    context = {
        'breakfast': breakfast,
        'lunch': lunch,
        'dinner': dinner,
        'snacks': snacks,
        'customers': customers,
    }

    if 'addToMyListButton' in request.POST:
        primaryKeyOfFood = request.POST['addToMyListButton']
        itemComplet = Food.objects.filter(pk=primaryKeyOfFood)
        for item in itemComplet:
            FoodInADay.objects.create(
                name=item.name,
                category=item.category,
                carbohydrate=item.carbohydrate,
                fats=item.fats,
                protein=item.protein,
                calorie=item.calorie,
                quantity=item.quantity,
            )
            #History.objects.crete(item)

    return render(request, 'calorie/fooditem.html', context)

# @login_required(login_url='login')
# @allowed_users(allowed_roles=['admin'])
def create_food_item(request):
    form = FoodForm()
    if request.method == 'POST':
        form = FoodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'calorie/createfooditem.html', context)


# @unauthorized_user
def register_page(request):
    form = CreateUserForm()
    if request.method == 'post':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='user')
            user.groups.add(group)
            email = form.cleaned_data.get('email')
            Customer.objects.create(user=user, name=username, email=email)
            messages.success(request, 'Account created for ' +username)
            return redirect('login')
    context = {'form': form}
    return render(request, 'calorie/register.html', context)


# @unauthorized_user
def login_page(request):
    if request.method == 'post':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'username or password is invalid')
    return render(request, 'calorie/login.html')



# @login_required(login_url='login')
def logout_user(request):
    logout(request)
    return redirect('login')


def user_page(request):
    user = request.user
    cust = user.customer
    food_items = Food.objects.filter()
    my_filter = FoodFilter(request.GET, queryset=food_items)
    food_items = my_filter.qs
    total = UserFood.objects.all()
    my_food_items = total.filter(customer=cust)
    cnt = my_food_items.count()
    query_set_food = []
    for food in my_food_items:
        query_set_food.append(food.fooditem.all())
    final_food_items = []
    for items in query_set_food:
        for food_items in items:
            final_food_items.append(food_items)
    total_calories = 0
    for foods in final_food_items:
        total_calories += foods.calorie

    calorie_left = 2000 - total_calories
    context = {
        'calorie_left': calorie_left,
        'total_calories': total_calories,
        'cnt': cnt,
        'food_list': final_food_items,
        'food_item': food_items,
        'my_filter': my_filter
    }

    return render(request, 'calorie/user.html', context)


def add_food_item(request):
    user = request.user
    cust = user.customer
    if request.method == "post":
        form = AddUserFood(request.POST)
        if form.is_valid():
            form.save()
            return redirect('food_item')
    form = AddUserFood()
    context = {'form': form}
    return render(request, 'calorie/adduserfooditem.html', context)

