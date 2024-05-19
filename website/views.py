from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Records
def home(request):
    record=Records.objects.all()
    # Check to see if logged in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been logged in')
            return redirect('home')
        else:
            messages.error(request, 'Invalid Login. Check your username or password again!')
            return redirect('home')
    else:
        return render(request, 'home.html', {'record':record})

def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():  # Corrected method name with parentheses
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, 'You have been successfully registered')
                return redirect('home')
            else:
                messages.error(request, 'User authentication failed after registration.')
                return redirect('register')

    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})

    return render(request, 'register.html', {'form': form})

def customer_record(request,pk):
    if request.user.is_authenticated:
        customer_record=Records.objects.get(id=pk)
        return render(request, 'record_detail.html', {'customer_record': customer_record})
    else:
        messages.error(request, 'You must be logged in first')
        return redirect(home)