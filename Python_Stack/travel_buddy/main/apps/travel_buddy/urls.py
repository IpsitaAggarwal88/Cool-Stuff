from django.conf.urls import url
from . import views

urlpatterns=[
	url(r'^$',views.index),
	url(r'^process$',views.process),
	url(r'^login$',views.login),
	url(r'^success$',views.success),
	url(r'^logout$',views.logout),
	url(r'^travels$',views.travels),
	url(r'^join/(?P<id>\d)$',views.join),
	url(r'^travels/plan$',views.add_plan),
	url(r'^travels/add$',views.add),
	url(r'^travels/destination/(?P<id>\d)$',views.destination),
]