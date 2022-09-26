"""p_0926 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from even import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index),
    path("number/<int:_number>/", views.print_number),
    path("print-text/", views.print_text),
    path("is-odd-even/<int:_even>/", views.even),
    path("four/<int:num1>/<int:num2>/", views.four),
    path("name/", views.name),
    path("prev-life/", views.prev_life),
    path("lorem-input/", views.lorem_input),
    path("lorem-check/", views.lorem_check),
]
