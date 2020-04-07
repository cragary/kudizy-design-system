from django.urls import path

from . import views

urlpatterns = [
    path('testingthisshit/', views.testingthisshit, name='testingthisshit'),
 ]
