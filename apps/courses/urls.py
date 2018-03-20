# _*_ coding: utf-8 _*_
__author__ = 'zhenzhen'
__date__ = '2018/3/20 19:29'

from django.conf.urls import url, include
from .views import CourseListView, CourseDetailView


app_name = 'course'
urlpatterns = [
    # 课程列表
    url(r'^list/$', CourseListView.as_view(), name='course_list'),
    # 课程详情页
    url(r'^detail/(?P<course_id>\d+)$', CourseDetailView.as_view(), name='course_detail'),

]










