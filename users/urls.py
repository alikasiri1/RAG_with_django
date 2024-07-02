from django.urls import path
from . import views


urlpatterns = [
    path('profile/' ,views.profile ,name = 'profile'),
    path('login/' , views.loginPage , name='login'),
    path('logout/' , views.logoutUser , name = 'logout'),
    path('register/' , views.registerUser , name='register'),

    ]