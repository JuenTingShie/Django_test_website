"""mysite URL Configuration

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
from mysite.views import here,math    #把mysite這個目錄下的views.py import進來
 
urlpatterns = [
	path('',here),    #預設的127.0.0.1:8000會到到的網頁
    path('admin/', admin.site.urls),
	path('here/',here),    # site/here/ 會帶到的網頁
	path('math/<int:a>/<int:b>/',math)    #利用網址進行運算
]
