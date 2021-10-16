from datetime import date
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.user',on_delete=models.CASCADE)
    image = models.ImageField(blank = True,null=True)
    caption = models.TextField()
    created_date = models.DateTimeField(default= timezone.now)

    


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default ='default.jpg',upload_to ='profile_pics')
    

    def __str__(self):
        return f'{self.user.username} Profile'
        

class Comment(models.Model):
    post = models.ForeignKey('Post',related_name='comments',on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.post.caption,self.name}'

