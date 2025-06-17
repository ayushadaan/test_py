from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path('', views.index, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"), 
    path('ice-cream/', views.ice_cream, name="ice_cream"),
    path('softy/', views.softy, name="softy"), 
    path('family-pack/', views.family_pack, name="family_pack"), 
    

]
