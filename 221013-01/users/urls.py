from django.urls import path
from . import views


app_name = 'user'
urlpatterns = [
    path('', views.main, name='main'),
    path('users/index/', views.index, name='index'),
    path('users/signup/', views.signup, name='signup'),
    path('users/login/', views.login, name='login'),
    path('users/logout/', views.logout, name='logout'),
    path('users/<int:pk>/', views.detail, name='detail'),
    path('users/update/', views.update, name='update'),
    path('users/delete/', views.delete, name='delete'),
    path('users/password/', views.set_password, name='set_password'),
]
