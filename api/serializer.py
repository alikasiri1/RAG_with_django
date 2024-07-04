from rest_framework import serializers
from Rag.models import Page
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class PageSerializer(serializers.ModelSerializer):
    user_profile = UserSerializer(many = False) # get the hole object instead  user_profile_id
    class Meta:  
        model = Page 
        fields = '__all__' #['title' , 'user_profile' , 'created_at'] 