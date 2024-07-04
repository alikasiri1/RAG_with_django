from django.db import models
from users.models import Profile
from django.contrib.auth.models import User
from django.db import models
import uuid
# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) #auto_now_add=True
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Page(models.Model):
    title = models.CharField(max_length=100 , null = True , blank = True ) 
    user_profile = models.ForeignKey(User, on_delete=models.CASCADE)
    # description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default = uuid.uuid4 , unique=True , primary_key = True , editable = False)

    def __str__(self):
        return self.title
    

class Question_and_Answer(models.Model):
    page = models.ForeignKey(Page, related_name='questions', on_delete=models.CASCADE)
    message = models.TextField()
    response = models.TextField()
    # vote_total = models.IntegerField(default=0 , null=True , blank=True)
    
    # created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.page.title

# class Answer(models.Model):
#     question = models.OneToOneField(Question, related_name='answer', on_delete=models.CASCADE)
#     text = models.TextField()
#     # created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.text