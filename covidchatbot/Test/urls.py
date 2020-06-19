from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.test),
    path('count/',views.count),
    #path('fund/',views.fund),
    path('contact/',views.contact),
    path('edit/',views.edit),
    path('get',views.get),
]