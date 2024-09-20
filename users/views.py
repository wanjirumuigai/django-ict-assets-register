from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout, login
from django.contrib import messages
# Create your views here.


def register(request):
    if request.method == 'POST':

        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account has been created for {username}. Continue to log in')

            return redirect('user-login')
    else:
        form = CreateUserForm()
    context = {
    'form': form
            }

    return render(request, 'users/register.html', context)


def user_logout(request):
    logout(request)
    return render(request, 'users/logout.html', {})

def login(request):
    print(request.user)
    if request.user:
        pass
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
        

            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('/')
            else:
                return redirect('login')
        

        else:
            return render(request, 'users/login.html')
    
def profile(request):
    return render(request, 'users/profile.html')


def profile_update(request):

    
    if request.method == 'POST':
        
            
        user_form = UserUpdateForm(request.POST,instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('user-profile')
               
        
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'user_form':user_form,
        'profile_form': profile_form
    }
    return render(request, 'users/profile_update.html', context)



   



