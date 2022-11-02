from celery.schedules import crontab
from django.http.response import HttpResponse
from django.shortcuts import render
from .tasks import test_func
from send_mail_app.tasks import send_mail_func
from django_celery_beat.models import PeriodicTask, CrontabSchedule
import json
from  controlCentre. models import BillingManager
from app .models import Transaction
from datetime import timedelta 
from django.contrib import messages
from django.utils import timezone





def schedule_billing(next_billing_date,business_ID):
     billingInfo  = BillingManager.objects.filter(business_ID = business_ID)
     datetime_zone  = timezone.now()
     second_billing_date     = timedelta(days=1)
     third_billing_date      = timedelta(days=3)
     forth_billing_date      = timedelta(days=5)
     account_suspension_date = timedelta(days=8)

     second_billing_date = second_billing_date + next_billing_date 
     third_billing_date  = third_billing_date  + next_billing_date
     forth_billing_date  = forth_billing_date  + next_billing_date
     account_suspension_date =  account_suspension_date + next_billing_date
     if billingInfo.exists():
        billingDetail   = BillingManager.objects.get(business_ID = business_ID)
        
        
        email_counter = int(billingDetail.emailCounter)
        email_counter = email_counter + 1
        billingInfo.update(
            emailCounter             = email_counter,  
            first_billing_date       = next_billing_date,
            second_billing_date      = second_billing_date,
            third_billing_date       = third_billing_date,
            account_suspension_date  = account_suspension_date
        )
         
    
        PeriodicTask.objects.filter(name = business_ID).delete()
     schedule, created = CrontabSchedule.objects.get_or_create(hour = 1,minute = 34)
     PeriodicTask.objects.create(crontab=schedule, name=, task='send_mail_app.tasks.send_mail_func',, args = json.dumps([1]))
    

     return HttpResponse("Done")