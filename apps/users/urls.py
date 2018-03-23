# _*_ coding: utf-8 _*_
__author__ = 'zhenzhen'
__date__ = '2018/3/23 12:23'

from django.conf.urls import url

from .views import UserInfoView


app_name = 'users'
urlpatterns = [
    # 用户信息
    url(r'^info/$', UserInfoView.as_view(), name='user_info'),
    ]