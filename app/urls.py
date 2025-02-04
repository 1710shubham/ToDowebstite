from django.urls import path,include
from . import views

urlpatterns = [
    path("/",views.Login,name="login"),
    path("register/",views.Register,name="register"),
    path("index/",views.Index,name="index"),

]
