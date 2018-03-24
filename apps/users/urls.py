# _*_ coding: utf-8 _*_
__author__ = 'zhenzhen'
__date__ = '2018/3/23 12:23'

from django.conf.urls import url

from .views import UserInfoView, UploadImageView, UpdatePwdView, SendEmailCodeView


app_name = 'users'
urlpatterns = [
    # 用户信息
    url(r'^info/$', UserInfoView.as_view(), name='user_info'),

    # 用户头像上传
    url(r'^image/upload/$', UploadImageView.as_view(), name='image_upload'),

    # 用户个人中心修改密码
    url(r'^update/pwd/$', UpdatePwdView.as_view(), name='update_pwd'),

    # 用户个人中心发送邮箱验证码
    url(r'^sendemail_code/$', SendEmailCodeView.as_view(), name='sendemail_code'),

]