"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [

    #path('', views.view),
    path('',views.logandregister),
    path('register',views.register, name='register'),
    path('login', views.signin, name='login'),
    path('out',views.signout, name='out'),
    path('home',views.loggedin),
    path('', views.view),
    path('dashboard',views.dashboard, name='dashboard'),
    #path('dash',views.empdisplay),
    path('fgo',views.dashboardforms, name='fgo'),
    path('eform',views.empregister, name='eform'),

    #path('lgo',views.userupdate, name='lgo'),

    path('brows',views.browsjobs, name='brows'),
    #path('service',views.services, name='service'),
    path('works',views.pages, name='works'),
    path('seller',views.psellers, name='seller'),

    path('faq',views.pfaq, name='faq'),
    path('hire/<int:pk>',views.workers, name='hire'),

    path('review/<int:pk>',views.review, name='review'),
    path('usrupdate',views.org_update, name='usrupdate'),
    path('update',views.profile_update_org, name='update'),
    #path('filter',views.filterr, name='filter'),
    path('empupdate',views.empupdate, name='empupdate'),
    path('emporgupdate',views.emp_org_update, name='emporgupdate'),
    path('about',views.about, name='about'),
    path('contact',views.contact, name='contact'),
    #path('Message/<int:pk>', views.chat, name='Message'),

    path('msg/<int:pk>',views.message, name='msg'),
    path('calendar',views.calendar, name='calendar'),
    path('chat',views.chat, name='chat'),
    path('index',views.view),
    path('professional',views.professional, name='professional'),
    path('local',views.local, name = 'local')



]
