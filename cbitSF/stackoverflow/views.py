from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm



def home(request):
    return render(request,'stackoverflow/base.html')

def base(request):
    return render(request,'stackoverflow/base.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'stackoverflow/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'stackoverflow/profile.html')

def qa(request):

    return render(request,'stackoverflow/qa.html')



