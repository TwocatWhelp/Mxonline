# _*_ coding: utf-8 _*_
__author__ = 'zhenzhen'
__date__ = '2018/3/14 22:16'

from django import forms


class LoginForm(forms.Form):
    # required为true时，这个字段不能为空，为空就会报错
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)






