from django.shortcuts import render, redirect
from .forms import UserRegistrationForm 

# Create your views here.

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('group')
    else:
        user_form = UserRegistrationForm()
        return render(request, 'users/register.html', {'form':user_form})