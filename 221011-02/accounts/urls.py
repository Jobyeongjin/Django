from django.urls import path
from . import views


app_name = 'account'
urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('<int:pk>/', views.detail, name='detail'),
]
