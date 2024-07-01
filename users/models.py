from django.db import models
from django.contrib.auth.models import User
import uuid 

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User , on_delete = models.CASCADE , null = True , blank = True)
    name = models.CharField(max_length=100 ,null = True , blank = True)
    username = models.CharField(max_length=100, null = True , blank = True)
    email = models.EmailField(max_length = 500)
    # profile_image = models.ImageField( null = True , blank = True , default='')\
    created = models.DateTimeField(auto_now_add = True)
    id = models.UUIDField(default = uuid.uuid4 , unique=True , primary_key = True , editable = False)

    def __str__(self) -> str:
        return str(self.user.username)
    
