# _*_ coding: utf-8 _*_
__author__ = 'zhenzhen'
__date__ = '2018/3/14 22:16'

from django import forms
from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    # required为true时，这个字段不能为空，为空就会报错
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=5)
    captcha = CaptchaField(error_messages={'invalid': '验证码错误'})




