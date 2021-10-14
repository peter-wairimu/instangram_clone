from django.urls import path
from .import views
from .views import (
    PostListView
)




urlpatterns =[

    path('register/',views.registerPage,name='register'),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.userPage,name='user-page'),
    path('user/',views.logoutUser,name='logout'),
    path('',views.logincup,name='auth'),
    path('',PostListView.as_view(),name='post_list'),


]