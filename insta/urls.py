from django.urls import path
from .import views


urlpatterns =[
    path('',views.logincup,name='auth'),


]