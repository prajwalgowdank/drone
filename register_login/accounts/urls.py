from unicodedata import name
from django.urls import path
from django.shortcuts import redirect
from .import views






from django.contrib import admin
from django.urls import path
from accounts import views
from django.views.i18n import JavaScriptCatalog

urlpatterns = [
    path('',views.index, name = 'index'),
    path('register/',views.registerUser,name='register'),
    path('login/',views.loginUser,name='login'),
    path('home/',views.home,name='home'),
    path('logout/',views.logoutUser, name='logout'),
    path('service/',views.service,name='service'),
    path('portfolio/',views.portfolio,name="portfolio"),
    path('clients/',views.clients,name="clients"),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('savedata/',views.saveEnquiry,name='savedata'),
    path('arial/',views.arial,name='arial'),
    path('video/',views.video,name='video'),
    path('mapping/',views.mapping,name='mapping'),


]