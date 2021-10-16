from datetime import date, datetime
from django.contrib.auth import forms
from django.http import request
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Post,Comment, Profile
from .decorators import unauthenticated_user
from .forms import CreateUserForm, UserUpdateForm, ProfileUpdateForm,PostForm,CommentForm
from django.contrib import messages
from django .contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone



# Create your views here.


@login_required(login_url='login')
def post(request):
    posts = Post.objects.all().filter(created_date__lte = timezone.now()).order_by('-created_date')




    return render(request,'post.html',{'posts':posts,})

@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Account was created for ' + user)
            return redirect('login')


    context = {'form': form}
    return render(request,'accounts/register.html',context)
@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request,username = username,password= password)
        if user is not None:
            login(request,user)
            return redirect('post_list')
            
        else:
            messages.info(request,'Username or password is inorrect')
            

    context = {}
    return render(request,'accounts/plogin.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')




def logincup(request):
    return render(request,'post.html')


def userPage(request):
    context = {}

    return render(request,'post.html',context)


@login_required(login_url='login')
def profile(request):
    user = request.user
    user = Profile.objects.get_or_create(user= request.user)
    
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)                         
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated successfully!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'user': user

    }

    return render(request, 'accounts/profile.html', context)


@login_required(login_url='login')
def create_post(request):
    current_user = request.user
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES)
        if form.is_valid:
            post = form.save(commit= False)
            post.author = current_user
            post.save()
        return redirect('post_list')
    else:
        form = PostForm()
    return render(request,'create_post.html',{'form':form})



    

def add_comment(request,pk):
    post = Post.objects.get(pk = pk)
    form = CommentForm(request.POST,instance=post)
    if request.method == "POST":
        if form.is_valid():
            name = request.user.username
            comment_body = form.cleaned_data['comment_body']
            peter = Comment(post=post,name =name,comment_body =comment_body,date_added=datetime.now())

            peter.save()
            return redirect('post_list')
        else:
            print('form is invalid')

    else:
        form = CommentForm

    context = {
        'form':form
    }
    return render(request,'tag.html',context)




