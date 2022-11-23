from django.urls import path
from testapp import views

urlpatterns = [
    path('users', views.index, name=" index"),
    path("users/<str:pk>", views.checkUsers, name="checkUsers"),
    path("unknown", views.resource, name="resource"),
    path("unknown/<str:pk>", views.checkResource, name="checkResource"),
    path("login", views.login, name="login"),
    path("register", views.register, name="register"),
    path("getResource", views.getResource, name="getResource"),
    path("getUser", views.getUser, name="getuser"),

]
