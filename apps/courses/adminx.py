# _*_ coding: utf-8 _*_
__author__ = 'zhenzhen'
__date__ = '2018/3/12 19:27'

import xadmin

from .models import Course, Lesson, Video, CourseResource, BannerCourse
from organization.models import CourseOrg


class LessonInline(object):
    model = Lesson
    extra = 0


class CourseResourceInline(object):
    model = CourseResource
    extra = 0


class CourseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums', 'add_time', 'get_zj_nums', 'go_to']
    search_fields = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums']
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums', 'add_time']
    # inlines = [LessonInline, CourseResourceInline]
    # style_fields = {"detail": "ueditor"}
    style_fields = {'detail': 'ueditor'}
    # 默认排序
    # ordering = ['-click_nums']
    # 不能随意更改
    # readonly_fields = ['click_nums', 'fav_nums']
    # 隐藏字段，和readonly_fields字段起冲突，只能存在一个
    # exclude = ['click_nums']
    # list_editable = ['degree', 'desc']
    # 设置定时刷新
    # refresh_times = [3, 5, 10]
    import_excel = True

    def queryset(self):
        qs = super(CourseAdmin, self).queryset()
        qs = qs.filter(is_banner=False)
        return qs

    def save_models(self):
        # 在保存课程的时候统计课程机构的课程数
        obj = self.new_obj
        obj.save()
        if obj.course_org is not None:
            course_org = obj.course_org
            course_org.course_nums = Course.objects.filter(course_org=course_org).count()
            course_org.save()

    def post(self, request, *args, **kwargs):
        if 'excel' in request.FILES:
            pass
        return super(CourseAdmin, self).post(request, args, kwargs)


class BannerCourseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums', 'add_time']
    search_fields = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums']
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums', 'add_time']
    inlines = [LessonInline, CourseResourceInline]
    # 默认排序
    ordering = ['-click_nums']
    # 不能随意更改
    # readonly_fields = ['click_nums', 'fav_nums']
    # 隐藏字段，和readonly_fields字段起冲突，只能存在一个
    # exclude = ['click_nums']

    def queryset(self):
        qs = super(BannerCourseAdmin, self).queryset()
        qs = qs.filter(is_banner=True)
        return qs



class LessonAdmin(object):
    list_display = ['name', 'course', 'add_time']
    search_fields = ['name', 'course']
    list_filter = ['name', 'course__name', 'add_time']


class VideoAdmin(object):
    list_display = ['name', 'lesson', 'add_time']
    search_fields = ['name', 'lesson']
    list_filter = ['name', 'lesson__name', 'add_time']


class CourseResourceAdmin(object):
    list_display = ['name', 'course', 'download', 'add_time']
    search_fields = ['name', 'course' 'download',]
    list_filter = ['name', 'course__name', 'download', 'add_time']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(BannerCourse, BannerCourseAdmin)


xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)

