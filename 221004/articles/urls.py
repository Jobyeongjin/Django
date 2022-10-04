from django.urls import path 
from . import views # 현재 폴더의 views와 연결하기


# URL namespace 사용함으로 업무 효율 높이기 💡
app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'), # 특정 pk값을 주소로 사용 💡
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/delete/', views.delete, name='delete'),
]