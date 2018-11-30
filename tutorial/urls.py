"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from app import views

urlpatterns = [
    path('dashboard',
         views.dashboard,
         name='dashboard'),
    path('tables',
         views.tables,
         name='tables'),
    path('a', views.a, name='a_url'),
    path('b', views.b, name='b_url'),
    path('admin/', admin.site.urls),
    path('index', views.index),
    path('user', views.user),
    path('detail/<int:pk>', views.DetailView.as_view(), name='detail'),
    path('list', views.ListView.as_view()),
    path('search', views.SearchFormView.as_view()),
    path('template', views.template)
]







