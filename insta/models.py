from datetime import date
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.user',on_delete=models.CASCADE,related_name='author')
    image = models.ImageField(blank = True,null=True)
    caption = models.TextField()
    created_date = models.DateTimeField(default= timezone.now)
    updated = models.DateTimeField(auto_now= True)
    liked = models.ManyToManyField(User, default=None,blank= True,related_name='liked')

    def __str__(self):
        return f'{self.author.username}'

    @property
    def num_likes(self):
        return self.liked.all().count

    @classmethod
    def search_category(cls,search):
        searches = cls.objects.filter(author__username__icontains = search)
        return searches

    


LIKE_CHOICES = (
    ('Like','Like'),
    ('Unlike','Unlike'),
)


class Like(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES,default='Like',max_length=10)

    def __str__(self):
        return str(self.post)



class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default ='default.jpg',upload_to ='profile_pics')
    

    def __str__(self):
        return f'{self.user.username} Profile'

    
        

class Comment(models.Model):
    post = models.ForeignKey('Post',related_name='comments',on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    comment_body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.post.caption,self.name}'


class FollowsCount(models.Model):
    follower = models.CharField(max_length=1000)
    user = models.CharField(max_length=1000)

    def __str__(self):
        return self.user











