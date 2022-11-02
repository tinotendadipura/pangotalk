from django.http import HttpResponse

from django.shortcuts import render , redirect , get_object_or_404,redirect

import datetime
import pytz
from datetime import timedelta
from . models import UserProfile,BusinessProfile
from django.contrib import messages


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func



def  user_controller(view_func):
    def wrapper_func(request,*args,**kwargs):
        if request.user.is_authenticated:
            farmer       = ['Farmer']
            adminstrator = ['Adminstrator']
            
            
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in farmer:
                return redirect('home/dashboard')
            if group in  adminstrator:
                return redirect('business-manager/admin')
            
            else:
                return view_func(request,*args,**kwargs)
        else: 
            return view_func(request,*args,**kwargs)

    return wrapper_func






def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return redirect('/')
        return wrapper_func
    return decorator





def allowed_account(allowed_account=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            user_status = UserProfile.objects.get(user = request.user)
            businessID  = user_status.business_ID
            info        = BusinessProfile.objects.get(business_ID = businessID)
            
            if info.category in allowed_account:
                return view_func(request, *args, **kwargs)
            else:
                return redirect('/')
        return wrapper_func
    return decorator



def  form_complete(view_func):
    def wrapper_func(request,*args,**kwargs):
        
        user_status = UserProfile.objects.get(user = request.user)
        businessID  = user_status.business_ID
        info = BusinessProfile.objects.get(business_ID = businessID)
        if info.businessprofile_status == False or info.businessCategory_status == False:
            if info.businessprofile_status == True:
                messages.info(request, "Please select your business category to proceed.")
                return redirect('account/user/business/category/business-type')
            else:
                messages.info(request, "Please complete your business profile to proceed.")
                return redirect('account/user/business/profile')
        
        else: 
             return view_func(request,*args,**kwargs)

    return wrapper_func


def  account_verification(view_func):
    def wrapper_func(request,*args,**kwargs):
        if request.user.is_authenticated:
            user_status = UserProfile.objects.get(user = request.user)
            businessID  = user_status.business_ID
            info = BusinessProfile.objects.get(business_ID = businessID)
            if info.account_authorisation_status == False :
                
                return redirect('/')
            
            else: 
                return view_func(request,*args,**kwargs)
        return redirect('/')
    return  wrapper_func
    

def category_access(view_func):
    def wrapper_func(request,*args,**kwargs):
        user_status = UserProfile.objects.get(user = request.user)
        businessID  = user_status.business_ID
        info = BusinessProfile.objects.get(business_ID = businessID)
        if info.category == 'RETAIL AND ECOMM':
            
            return redirect('e-commerce/home/dashboard')
        
        elif info.category == 'CAR RENTAL':
            return redirect('account/user/business/signup-complete')   
            
        elif info.category == 'CAR REPAIR':
            return redirect('account/user/business/signup-complete')  


        elif info.category == 'DRIVING SCHOOL':
            return redirect('account/user/business/signup-complete')  
    return wrapper_func
    


  