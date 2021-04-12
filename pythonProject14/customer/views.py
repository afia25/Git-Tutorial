from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .form import *
#from . import loaddata
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user,authenticate,login
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *

def customerInfo(request):
    customers=Customer.objects.filter(delivary_address__icontains='Mohammadpur')
    return render(request,'user/customerInfo.html',{'customers':customers})

def user_Details(request):
    if (request.method=='POST'):
        userdetailsform = UserDetailsForm(request.POST)
        if (userdetailsform.is_valid()):
            userdetailsform.save()
            return redirect('profile')

        else:
            context = {
                'userdetailsform': UserDetailsForm
            }
            return render(request, 'customer/user_Details.html', context)

    else:
        userdetailsform = UserDetailsForm()
        context = {
            'userdetailsform': UserDetailsForm
        }
        return render(request, 'customer/user_Details.html', context)






@login_required
def profile(request):
    user=get_user(request)

    context={
        'name':user.username,
        'email':user.email
    }
    return render(request,'customer/profile.html',context)


#@login_required
def profileUpdate(request):
    if (request.method == "POST"):
        user_update_form = UserUpdateForm(request.POST,instance=request.user)
        #profile_update_form = ProfileUpdateForm(request.POST,instance=request.user.profile)
        #if (user_update_form.is_valid() and profile_update_form.is_valid()):
        if (user_update_form.is_valid()):
            user_update_form.save()
            #profile_update_form.save()
            return redirect('profile')
        else:
            context = {
                'user_update_form': user_update_form,
                #'profile_update_form': profile_update_form

            }
            return render(request, 'customer/profileUpdate.html', context)

    else:
        user_update_form = UserUpdateForm()
        #profile_update_form = ProfileUpdateForm()
        context = {
            'user_update_form': user_update_form,
            #'profile_update_form': profile_update_form

        }
        return render(request, 'customer/profileUpdate.html', context)






def register(request):
    if (request.method=="POST"):
        form=UserRegistrationForm(request.POST)
        profileform = RegistrationProfileForm(request.POST)
        if (form.is_valid() and profileform.is_valid()):
            error=''
            dict=request.POST
            username=dict['username']
            check=User.objects.filter(username='username')
            if len(check)==0:
                form.save()
                profileform.save()

            else:
                error='Username already exists.'
                return render(request, 'customer/register.html', {'form':form,'error':error})

            user = get_user(request)
            #username='Naima'
            #username=form.cleaned_data.get(user.username)
            #password='uap123456'
            #password = form.cleaned_data.get(user.password)
            #new_user=authenticate(username=username,password=password)
            #login(request,new_user)

            message='Welcome to Inventory Management System'
            messages.success(request, message=message)
            return redirect('home')
        else:
            context={
                'form':form
            }
            return render(request, 'customer/register.html', context)

    else:
        form = UserRegistrationForm()
        profileform=RegistrationProfileForm()
        return render(request, 'customer/register.html', {'form':form,'profileform':profileform})

    #return render(request, 'user/register.html', {'form':form})
@login_required
def home(request):
    return render(request,'customer/home.html')



def base(request):
    return render(request,'customer/base.html')



