from django.shortcuts import render , redirect
from django.contrib.auth import login , authenticate , logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
@login_required(login_url='login') # if user has not loged in go to the login page instead of profile page
def profile(request):
    if request.user.is_authenticated:
        user = request.user
        print(user.email)
        return render(request , 'users/profile.html' , {'user' : user.username})
    else:
        return redirect('login')

def loginPage(request):

    if request.user.is_authenticated:
        return redirect('home_page')
    if request.method == 'POST':
        print(request.POST)
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request , " username dose not exist")
        
        user = authenticate(request , username=username , password=password)
        
        if user is not None:
            print(user.username , '\n\n\n\n')
            login(request , user)
            return redirect('home_page')
        else:
            messages.error(request ,'username or password is incorrect')

    return render(request , 'users/login_register.html')

def logoutUser(request):
    logout(request)
    return redirect('home_page')