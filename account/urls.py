from django.urls import path

from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('password', views.change_password, name='password'),
    path('user_update', views.UserUpdate.as_view(), name='user_update'),
    path('pg13_update', views.Pg13Update.as_view(), name='pg13_update'),
]
