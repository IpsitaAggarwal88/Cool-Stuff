# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.contrib import messages

from models import *
import bcrypt
import datetime
# Create your views here.
def index(request):
	if(not(request.session.get('id'))):
		request.session['id']=0
	
	return render(request,"travel_buddy/index.html")

def process(request):
	errors=User.objects.basic_validator(request.POST)
	if len(errors):
		for error in errors.itervalues():
			messages.error(request,error)
		request.session['id']=0
		return redirect('/')
	else:
		user=User.objects.filter(email=request.POST['email'])
		if user:
			messages.error(request,'User aready exists! ')
			return redirect('/')
		else:
			hash1=bcrypt.hashpw(request.POST['password'].encode(),bcrypt.gensalt())

			user=User.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'],email=request.POST['email'],password=hash1)
		
			request.session['id']=user.id
		return redirect('/success')

def login(request):
	errors=User.objects.login_validator(request.POST)
	if len(errors):
		for error in errors.itervalues():
			messages.error(request,error)
	users=User.objects.filter(email=request.POST['email'])
	for val in users:
		request.session['id']=val.id
	print users
	if not(users):
		messages.error(request,'User not registered!')
		
		return redirect('/')
	else:
		for val in users:
			check=bcrypt.checkpw(request.POST['password'].encode(),val.password.encode())
			print check
			if check==False:
				messages.error(request,'wrong password!')
				return redirect('/')
				
		return redirect('/success')
		

def success(request):
	return redirect('/travels')

def logout(request):
	request.session.pop('id')
	return redirect('/')

def travels(request):
	user=User.objects.get(id=request.session['id'])
	user_trips=user.trips_created.all()
	user_joined_trips=user.trips.all()
	trips=Trip.objects.all()
	trips=Trip.objects.exclude(users=user)
	
		
	context={
	'user':user,
	'user_joined_trips':user_joined_trips,
	'user_trips':user_trips,
	'trips':trips
	}
	return render(request,"travel_buddy/travels.html",context)

def join(request,id):
	trip=Trip.objects.get(id=id)
	user=User.objects.get(id=request.session['id'])
	joined_trips=user.trips.all()
	created_trip=user.trips_created.all()
	if (trip not in created_trip) and (trip not in joined_trips):
		user.trips.add(trip)
	return redirect('/travels')

def add_plan(request):
	return render(request,"travel_buddy/travels-add.html")

def add(request):
	user=User.objects.get(id=request.session['id'])
	trip=Trip.objects.create(destination=request.POST['destination'],description=request.POST['description'],travel_from=request.POST['travel_from'],travel_to=request.POST['travel_to'],user=user)
	
	return redirect('/travels')
def destination(request,id):
	trip=Trip.objects.get(id=id)
	username=trip.user.first_name
	users=trip.users.exclude(first_name=username)
	
	context={
	'trip':trip,
	'users':users
	}
	return render(request,"travel_buddy/destination.html",context)


