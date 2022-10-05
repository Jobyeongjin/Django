from django.urls import path
from . import views # 현재 폴더의 views.py 연결하기


app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'), # 특정 pk 값을 주소로 활용 💡
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/delete/', views.delete, name='delete'),
]



