# _*_ coding: utf-8 _*_
__author__ = 'zhenzhen'
__date__ = '2018/3/20 19:29'

from django.conf.urls import url, include
from .views import CourseListView, CourseDetailView, CourseInfoView, CommentView, AddCommentView, VideoPlayView


app_name = 'course'
urlpatterns = [
    # 课程列表
    url(r'^list/$', CourseListView.as_view(), name='course_list'),

    # 课程详情页
    url(r'^detail/(?P<course_id>\d+)$', CourseDetailView.as_view(), name='course_detail'),

    # 课程章节信息
    url(r'^info/(?P<course_id>\d+)$', CourseInfoView.as_view(), name='course_info'),

    # 课程评论信息
    url(r'^comment/(?P<course_id>\d+)$', CommentView.as_view(), name='course_comment'),

    # 添加课程评论
    url(r'^add_comment/$', AddCommentView.as_view(), name='add_comment'),

    # 课程评论信息
    url(r'^video/(?P<video_id>\d+)$', VideoPlayView.as_view(), name='video_play'),


]










