"""iclock URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from test1 import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^upload/$', views.uploadUserInfo, name='upload'),
    url(r'^$', views.index),
    url(r'^iclock/cdata$', views.cdata, name="cdata"),
    url(r'^iclock/setrequest$', views.setrequest, name="setrequest"),
    url(r'^iclock/getrequest$', views.getrequest, name="getrequest"),
    url(r'^iclock/devicecmd$', views.devicecmd, name="devicecmd"),
]
