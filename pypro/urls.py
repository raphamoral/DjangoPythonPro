"""pypro URL Configuration

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
from django.conf.urls.static import static
from django.contrib import admin
from django.http import request
from django.template.defaulttags import url
from django.urls import path, re_path, include

from pypro.base import views
from pypro.base.views import webhook

urlpatterns = [
    path('admin/', admin.site.urls),
    #path(r'^webhook/(page-(\d+)/)?$', webhook_request)
#path('', views.webhook(request), name='webhook_request')
   #
   path('webhook/',views.webhook)
   # path('webhook/', include('views.webohook_request'))


 #  url('api/webhook_request', views.webhook_request, name='webhook_request'),


#path('',home ),
]
