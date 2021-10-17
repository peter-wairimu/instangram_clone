from django.contrib import admin
from .models import Comment, Post,Profile,Like,FollowsCount
# Register your models here.

admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(FollowsCount)

