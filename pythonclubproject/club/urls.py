
from django.urls import path
from .import views


urlpatterns = [
    path('', views.index, name='index'),
    path('clubresources/', views.clubresources, name='resource'),
    path('getmeeting/', views.getmeeting, name='getmeeting'),
    path('meetingdetail/<int:id>', views.meetingdetail, name='details'),
    path('newresource/', views.newResource, name='newResource'),  
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]