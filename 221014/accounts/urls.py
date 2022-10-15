from django.urls import path
from . import views


app_name = 'account'
urlpatterns = [
    path('', views.main, name='main'),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/login/', views.login, name='login'),
    path('accounts/logout/', views.logout, name='logout'),
    path('accounts/index/', views.index, name='index'),
    path('accounts/<int:pk>/', views.detail, name='detail'),
    path('accounts/update/', views.update, name='update'),
    path('accounts/password/', views.set_password, name='set_password'),
    path('accounts/delete/', views.delete, name='delete'),
]
