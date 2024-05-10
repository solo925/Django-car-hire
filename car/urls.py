from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("details/",views.details,name="details"),
    path("book/",views.book,name="book"),
    path("login/",views.Login,name="login"),
    path("logout/",views.Logout,name="logout"),
    path("register/",views.register,name="register"),
    path("receipt/",views.receipt,name="receipt"),
    
]
