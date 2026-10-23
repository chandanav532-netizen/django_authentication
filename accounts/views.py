from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def login_view(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user!=None:
            login(request,user)
            messages.success(request,f'welcome"{user.username}"')
            return redirect('home')
        else:
            messages.error(request,"Invalid username and password")
    return render(request,'login.html')
        
def logout_view(request):
    logout(request)
    messages.info(request,"you have logged out successfully!")
    return redirect('login')
@login_required
def home(request):
    return render(request,'home.html')