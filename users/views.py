from django.shortcuts import render, redirect
from django.contrib import messages
from users.forms import UserRegisterForm


def register_page(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Hello, {username}")

            return redirect('food_item')
    else:
        form = UserRegisterForm()

    context = {
        'form': form,
    }
    return render(request, 'users/register.html', context)