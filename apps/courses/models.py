from datetime import datetime

from django.db import models

from organization.models import CourseOrg, Teacher

# Create your models here.


class Course(models.Model):
    course_org = models.ForeignKey(CourseOrg, verbose_name=u'课程机构', on_delete=models.CASCADE, null=True, blank=True)
    teacher = models.ForeignKey(Teacher, verbose_name=u'讲师', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50, verbose_name=u'课程名')
    desc = models.CharField(max_length=300, verbose_name=u'描述', default=u'')
    detail = models.TextField(verbose_name=u'课程详情')
    degree = models.CharField(choices=(('cj', u'初级'), ('zj', u'中级'), ('gj', u'高级')), max_length=10, verbose_name=u'难度')
    learn_times = models.IntegerField(default=0, verbose_name=u'学习时长（分钟时）')
    students = models.IntegerField(default=0, verbose_name=u'学习人数')
    fav_nums = models.IntegerField(default=0, verbose_name=u'收藏人数')
    image = models.ImageField(upload_to='courses/%Y/%m', verbose_name=u'封面图', max_length=200)
    click_nums = models.IntegerField(default=0, verbose_name=u'点击数')
    category = models.CharField(max_length=20, verbose_name=u'章节类别', default='后端开发')
    tag = models.CharField(default='', verbose_name=u'课程标签', max_length=20)
    youneed_know = models.CharField(max_length=300, verbose_name=u'课程须知', default=u'')
    teacher_tell = models.CharField(max_length=300, verbose_name=u'老师告诉你', default=u'')

    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'课程'
        verbose_name_plural = verbose_name

    def get_zj_nums(self):
        # 获取章节数
        return self.lesson_set.all().count()

    def get_learn_users(self):
        # 获取学习该课程的用户
        return self.usercourse_set.all()[:5]

    def get_course_lesson(self):
        # 获取课程所有章节
        return self.lesson_set.all()

    def __str__(self):
        return self.name


class Lesson(models.Model):
    course = models.ForeignKey(Course, verbose_name=u'课程', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name=u'章节名')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'章节'
        verbose_name_plural = verbose_name

    def get_lesson_video(self):
        # 获取章节下所有视频
        return self.video_set.all()

    def __str__(self):
        return self.name


class Video(models.Model):
    lesson = models.ForeignKey(Lesson, verbose_name=u'视频', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name=u'视频名称')
    learn_times = models.IntegerField(default=0, verbose_name=u'学习时长（分钟时）')
    url = models.CharField(max_length=300, verbose_name=u'访问地址', default='')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'视频'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseResource(models.Model):
    course = models.ForeignKey(Course, verbose_name=u'资源', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name=u'名称')
    download = models.FileField(upload_to='course/resource/%Y/%m', verbose_name=u'资源文件', max_length=200)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'资源'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name










































































