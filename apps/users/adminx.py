# _*_ coding: utf-8 _*_
__author__ = 'zhenzhen'
__date__ = '2018/3/12 19:09'

import xadmin
from xadmin import views

from .models import EmailVerifyRecord, Banner


# 全局设置
class BaseSetting(object):
    # 主题设定
    enable_themes = True
    use_bootswatch = True


# 全局设置 页头和页脚设置
class GlobalSetting(object):
    site_title = "慕学后台管理系统"
    site_footer = "慕学在线网"

    # 目录收起来
    menu_style = 'accordion'


class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']

xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)

