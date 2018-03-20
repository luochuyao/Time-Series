"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
# from django.urls import path
from django.conf.urls import url
from cmdb import views
import cmdb
# import dataProcess
#url函数可选参数kwargs：视图使用的字典类型的参数以及name：用来反向获取URl
urlpatterns = [
    #path('admin/', admin.site.urls),
    #url(r'^index/', views.index),
    url(r'^index', cmdb.views.index_1),
    url(r'^signalpointdata', cmdb.views.receive_data),
]
