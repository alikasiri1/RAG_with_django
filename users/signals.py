from django.db.models.signals import post_save , post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile

@receiver(post_save , sender=User)# ==  post_save.connect(User , sender=Profile)

def createProfile(sender , instance , created , **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user = user,
            username = user.username,
            email = user.email,
            name = user.first_name,
        )
    else: # updated
        user = instance
        profile = Profile.objects.get(user_id = user.id)
        profile.username = user.username
        profile.email = user.email
        profile.name = user.first_name
        print('profile has updated')
        profile.save()

    print('sender:' ,sender)
    print('instance:' ,instance)
    print('created:' ,created) # its ture when a new user creat a profile


def deleteUser(sender , instance  , **kwargs):
    print(f'user {instance} deleted')


# post_delete.connect(deleteUser , sender=Profile)