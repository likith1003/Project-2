from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('',views.index,name='index'),
    path('pythond',views.pythond,name='pythond'),
    path('pythonmt',views.pythonmt,name='pythonmt'),
    path('pythonat',views.pythonat,name='pythonat'),
    path('sql',views.sql,name='sql'),
    path('web',views.web,name='web'),
    path('apti',views.apti,name='apti'),
    path('verbal',views.verbal,name='verbal'),
    path('contact',views.contact,name='contact'),
    path('placements',views.placements,name='placements'),
    path('fresher',views.fresher,name='fresher')
]