"""MxOnline URL Configuration

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
from django.urls import path
from django.conf.urls import url, include

# 专门处理静态文件
from django.views.generic import TemplateView
import xadmin

from users.views import LoginView, RegisterView, ActiveUserView

urlpatterns = [
    path('xadmin/', xadmin.site.urls),

    url('^$', TemplateView.as_view(template_name='index.html'), name='index'),
    url('^login/$', LoginView.as_view(), name='login'),
    url('^register/$', RegisterView.as_view(), name='register'),

    # 图片认证验证码
    url(r'^captcha/', include('captcha.urls')),

    url(r'^active/(?P<active_code>.*)/$', ActiveUserView.as_view(), name='user_active'),

]
