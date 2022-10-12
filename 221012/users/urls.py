from django.urls import path
from . import views

app_name = 'user'
urlpatterns = [
    path('', views.main, name='main'),
    path('users/signup/', views.signup, name='signup'),
    path('users/', views.index, name='index'),
    path('users/<int:pk>', views.detail, name='detail'),
    path('users/login/', views.login, name='login'),
    path('users/logout/', views.logout, name='logout'),
]
