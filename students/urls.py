
from django.urls import path
from . import views
urlpatterns = [
    
    path('',views.index),
    path('contact',views.contact),
    path('students',views.students) ,
    path('students/<str:name>/<int:id>',views.details),
]
