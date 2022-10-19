from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('', views.main, name='main'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('<int:pk>/', views.detail, name='detail'),
]