from django.shortcuts import redirect, render
from accounts.forms import CreateUserForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.
def register(request):
    form=CreateUserForm
    if request.method == 'POST':
         form=CreateUserForm(request.POST)
         if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,"Accounts was created for " +user)
            return redirect('signin')
    context={'form':form}
    return render(request,'register.html',context)


def signin(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        
        if user is not None:
            login(request,user)
            return redirect('product')
        else:
            messages.info(request,'username or pasword error')
    return render(request,'login.html')
def logoutuser(request):
    logout(request)
    return redirect('signin')