from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('domains/',views.showdomains,name="showdomains"),
    path('adddomain/<domain>/<publicip>/<privateip>/',views.adddomains,name="adddomain"),
    path('addrecord/<domain>/<zonetype>/<recordtype>/<key>/<value>/',views.addrecord,name="addrecord"),
    path('showrecords/<domain>/',views.showrecords,name="showrecords"),
    path('deleterecord/<domain>/<recordname>/<recordtype>/',views.deleterecord,name="deleterecord"),
    path('refresh/<domain>/',views.refresh,name="refresh"),
]
