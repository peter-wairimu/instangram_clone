from django.urls import path
from .import views


from django.conf import settings
from django.conf.urls.static import static



urlpatterns =[

    path('register/',views.registerPage,name='register'),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.userPage,name='user-page'),
    path('user/',views.logoutUser,name='logout'),
    path('profile/', views.profile, name='profile'),
    path('post/', views.post, name='post_list'),
    path('',views.logincup,name='auth'),
   


]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    