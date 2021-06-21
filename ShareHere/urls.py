from django.contrib import admin
from django.urls import path
from ShareHere import views

urlpatterns = [
    path("", views.index),
    path("", views.index, name="index"),
    path("INT213", views.subject1, name= "INT213"),
    path("CSE211", views.subject2, name= "CSE211"),
    path("MTH401", views.subject3, name= "MTH401"),
    path("CSE205", views.subject4, name= "CSE205"),
    path("CSE320", views.subject5, name= "CSE320"),
    path("INT208", views.subject6, name= "INT208"),

]   