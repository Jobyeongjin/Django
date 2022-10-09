from django.urls import path
from . import views


app_name = 'review'
urlpatterns = [
    path('', views.main, name='main'),
    path('index/', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('<int:pk>/create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/delete/', views.delete, name='delete'),
]
