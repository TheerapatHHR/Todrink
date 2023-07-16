from django.urls import path
from . import views

#add = add customer
urlpatterns = [
    path('', views.home, name ='home'),   #'url link', views.(def function name), name = 'declair name to use in template'
    path('/history', views.history, name ='history'),
]