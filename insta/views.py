from django.shortcuts import render

# Create your views here.

def logincup(request):
    return render(request,'index.html')