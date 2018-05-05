# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re
import datetime
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your models here.
class UserManager(models.Manager):
	def basic_validator(self,postData):
		errors={}
		if len(postData['first_name'])<1:
			errors['first_name']="First name cannot be left empty"
		elif not(postData['first_name'].isalpha()):
			errors['first_name']="first name can only be alphabets"
		elif len(postData['first_name'])<3:
			errors['first_name']="First name can't be less than 2 characters"
		if len(postData['last_name'])<1:
			errors['last_name']="Last name cannot be left empty"		
		elif not(postData['last_name'].isalpha()):
			errors['last_name']="Last name can only be alphabets"
		elif len(postData['last_name'])<3:
			errors['last_name']="Last name can't be less than 2 characters"				
		
		if len(postData['email'])<1:
			errors['email']="Email cannot be left empty!"
		elif not EMAIL_REGEX.match(postData['email']):
			errors['bademail']="invalid email!"
		if len(postData['password'])<8:
			errors['password']="Password has to be minimum 8 characters"
		if postData['password']!=postData['cpwd']:
			errors['cpwd']="Password and confirm password don't match!"
		return errors
	def login_validator(self,postData):
		errors={}
		if len(postData['email'])<1:
			errors['email']="Email cannot be left empty!"
		elif not EMAIL_REGEX.match(postData['email']):
			errors['bademail']="invalid email!"
		return errors
	# def travel_validator(self,postData):
	# 	errors={}
	# 	if len(postData['destination'])<1:
	# 		errors['destination']="Destination cannot be left empty"
	# 	if len(postData['description'])<1:
	# 		errors['description']="description cannot be left blank"
	# 	if len(postData['travel_from'])<1:
	# 		errors['travel_from']="Travel from cannot be left blank"
	# 	if len(postData['travel_to'])<1:
	# 		errors['travel_to']="Travel To cannot be left blank"

	# 	if postData['travel_from']>postData['travel_to']:
	# 		errors['travel']="Travel from has to be before travel to!!"
	# 	return errors
class User(models.Model):
	first_name=models.CharField(max_length=25)
	last_name=models.CharField(max_length=25)
	email=models.CharField(max_length=40)
	password=models.CharField(max_length=15)
	def __repr__(self):
		return "<User Object: {} {} {} {}".format(self.first_name,self.last_name,self.email,self.password)
	objects=UserManager()

class Trip(models.Model):
	destination=models.CharField(max_length=50)
	description=models.TextField()
	travel_from=models.DateTimeField()
	travel_to=models.DateTimeField()
	user=models.ForeignKey(User,related_name="trips_created")
	users=models.ManyToManyField(User,related_name="trips")
	def __repr__(self):
		return "<Trip Object: {} {} {} {}>".format(self.destination,self.description,self.travel_from,self.travel_to)
