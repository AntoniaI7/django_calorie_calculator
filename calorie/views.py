from django.shortcuts import render
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import *
from django.contrib.auth.models import Group



def home(request):
    return HttpResponse('<h1>Calorie Calculator</h1>')


@login_required(login_url='login')
@admin_only
def home(request):
    breakfast = Category.objects.filter(name='breakfast')[0].fooditem_set.all()[:5]
    lunch = Category.objects.filter(name='lunch')[0].fooditem_set.all()[:5]
    dinner = Category.objects.filter(name='dinner')[0].fooditem_set.all()[:5]
    snacks = Category.objects.filter(name='snacks')[0].fooditem_set.all()[:5]
    customers = Customer.objects.all()
    context = {'breakfast': breakfast,
               'lunch': lunch,
               'dinner': dinner,
               'snacks': snacks,
               'customers': customers,
               }
    return render(request,'base.html',context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def fooditem(request):
    breakfast = Category.objects.filter(name='breakfast')[0].fooditem_set.all()
    b_cnt = breakfast.count()
    lunch = Category.objects.filter(name='lunch')[0].fooditem_set.all()
    l_cnt = lunch.count()
    dinner = Category.objects.filter(name='dinner')[0].fooditem_set.all()
    d_cnt = dinner.count()
    snacks = Category.objects.filter(name='snacks')[0].fooditem_set.all()
    s_cnt = snacks.count()
    context = {'breakfast': breakfast,
               'b_cnt': b_cnt,
               'l_cnt': l_cnt,
               's_cnt': s_cnt,
               'd_cnt': d_cnt,
               'lunch': lunch,
               'dinner': dinner,
               'snacks': snacks,
               }
    return render(request,'fooditem.html',context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createfooditem(request):
    form = FoodForm()
    if request.method == 'POST':
        form = FoodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'createfooditem.html', context)


@unauthorized_user
def registerPage(request):
    form = CreateUserForm()
    if request.method=='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='user')
            user.groups.add(group)
            email = form.cleaned_data.get('email')
            Customer.objects.create(user=user, name=username,email=email)
            messages.success(request,'Account created for '+username)
            return redirect('login')
    context={'form': form}
    return render(request, 'register.html', context)


@unauthorized_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'username or password is invalid')
    return render(request, 'login.html')



@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login')


def userPage(request):
    user = request.user
    cust = user.customer
    food_items = Food.objects.filter()
    my_filter = fooditemFilter(request.GET, queryset= food_items)
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
    context = {'calorie_left': calorie_left, 'total_calories': total_calories, 'cnt': cnt, 'food_list': final_food_items, 'food_item': food_items, 'my_filter': my_filter}
    return render(request, 'user.html', context)


def addFooditem(request):
    user = request.user
    cust = user.customer
    if request.method == "POST":
        form = AddUserFood(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    form = AddUserFood()
    context={'form': form}
    return render(request, 'addUserFooditem.html', context)