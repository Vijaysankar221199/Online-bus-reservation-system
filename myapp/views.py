from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404, redirect
from django import template
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from datetime import datetime
from django.db import transaction
from myapp.forms import Authentic
from django.conf import settings
from django.contrib import messages
import os
from .forms import *
from .models import *
import time
import base64
from django.utils import timezone
from django.core.mail import EmailMessage
import time


def index(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return render(request,'security.html',)
        else:
            return render(request,'inmates.html',)
    else:
        return render(request,'index.html',)


@login_required
def dashboard(request):
    if request.user.is_superuser:
        return render(request,'security.html',)
    else:
        return render(request,'inmates.html',)

@login_required
def book(request):
    if request.method == 'POST':
        slot_req_name = request.POST.get("seatname")
        str(slot_req_name)
        if slot_req_name is None:
            return HttpResponse("Select atleast one seat", content_type='text/plain')
        elif seats.objects.filter(slot_name= slot_req_name):
            return HttpResponse("already booked by another person. try another one", content_type='text/plain')
        else:
            username = request.user.username
            store_nowl = seats.objects.create(slot_name= slot_req_name,visiname=username,status='occupied')
            store_all = allbookings.objects.create(slot_name= slot_req_name,visiname=username,status='occupied')
            return HttpResponse("Booked", content_type='text/plain')
    else:
        status = seats.objects.filter(status='occupied')
        stu = {"details": status}
        return render(request,'book.html',stu)

@login_required
def mybookings(request):
    if request.user.is_superuser:
        return HttpResponse("NOT VALID", content_type='text/plain')
    else:
        if request.method == 'GET':
            #print("hai")
            username = request.user.username
            Image2 = seats.objects.filter(visiname= username)
            stu = {"details": Image2 }
            return render(request,'mybook.html',stu)

@login_required
def currentbookings_admin(request):
    if request.user.is_superuser:
        if request.method == 'GET':
            username = request.user.username
            Image2 = seats.objects.all()
            stu = {"details": Image2 }
            return render(request,'currentbooking_admin.html',stu)
        else:
            if 'RESET' in request.POST:
                instance = seats.objects.all()
                instance.delete()
                return HttpResponse("RESETED", content_type='text/plain')
    else:
        return HttpResponse("NOT VALID", content_type='text/plain')



@login_required
def allbookings_admin(request):
	if request.user.is_superuser:
		if request.method == 'GET':
			Image3 = allbookings.objects.all()
			stu = {"details":Image3}
			return render(request,'allbookings_admin.html', stu)



@login_required
def user_logout(request):
    #instance = allbookings.objects.all()
    #instance.delete()
    logout(request)
    return HttpResponseRedirect(reverse('index'))


# Create your views here.
def user_login(request):
    if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('index'))
    else:
        if request.method=="POST":
            username=request.POST.get("username")
            password=request.POST.get("password")

            user=authenticate(username=username,password=password)

            if user:
                login(request,user)
                return HttpResponseRedirect(reverse('index',))
            else:
                return HttpResponse("invalid username and password")
        else :
            return render(request,'login.html',)


def authentication_view(request):
    registered = False

    if request.method=="POST":
        #print(request.POST)
        auth=Authentic(request.POST )

        if auth.is_valid():
            auth=auth.save(commit=False)
            auth.set_password(auth.password)
            #hashing the password
            auth.save()
            registered=True
        else :
            print("error")
    else:
        auth=Authentic()
    return render(request,'login.html',)
