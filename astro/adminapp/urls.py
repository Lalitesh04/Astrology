from django.urls import path

from . import views
urlpatterns = [
    path('adminchangepwd', views.adminchangepwd, name="adminchangepwd"),
    path('viewdonations', views.viewdonations, name="viewdonations"),
    path('users', views.users, name="users"),
    path('adduser', views.adduser, name="adduser"),
]
