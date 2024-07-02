from django.shortcuts import render , redirect
from django.contrib.auth import login , authenticate , logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import  AuthenticationForm
from .forms import CustomUserCreationForm
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
    page = 'login'
    form = AuthenticationForm()
    context = {'page' : page , 'form': form}
    
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
            # messages.info(request, f"You are now logged in as {username}.")
            return redirect('home_page')
        else:
            messages.error(request ,'username or password is incorrect')

    return render(request , 'users/login_register.html' , context)

def logoutUser(request):
    logout(request)
    return redirect('home_page')


def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()#UserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)#UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False) # for preproces on user information befor save it into the db
            user.username = user.username.lower()
            user.save()

            messages.success(request , 'User accout was created!')

            login(request , user) # creat a cooki for user and known user as a loged in user
            return redirect('home_page')
        else:
            for error in form.errors.values():
                messages.error(request, error)
            # messages.error(request , 'An error has occurred during registration')
    context = {'page' : page , 'form' : form}
    return render(request , 'users/login_register.html' , context)