"""sample4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,include
from sampleapp import views
from sampleapp.views import SignUp,BooksDetailView,BookCheckOutView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.base,name='listpage'),
    path('index/',views.index),
    path('accounts/',include("django.contrib.auth.urls")),
    path('signup/',SignUp.as_view()),
    path('logout/',views.logout),
    path('details/<int:pk>/',BooksDetailView.as_view()),
    path('<int:pk>/checkout/',BookCheckOutView.as_view()),
]
    