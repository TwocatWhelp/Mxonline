# _*_ coding: utf-8 _*_
__author__ = 'zhenzhen'
__date__ = '2018/3/15 10:40'

from random import Random
from django.core.mail import send_mail

from users.models import EmailVerifyRecord
from MxOnline.settings import EMAIL_FROM


def send_register_email(email, send_type='register'):
    email_record = EmailVerifyRecord()
    code = generate_random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    email_title = ""
    email_boby = ""

    if send_type == 'register':
        email_title = '慕学在线网注册激活链接'
        email_boby = '请点击下面的链接激活你的链接: http://127.0.0.1:8000/active/{0}'.format(code)

        send_status = send_mail(email_title, email_boby, EMAIL_FROM, [email])
        if send_status:
            pass
    if send_type == 'forget':
        email_title = '慕学在线网密码重置链接'
        email_boby = '请点击下面的链接重置你的密码: http://127.0.0.1:8000/reset/{0}'.format(code)

        send_status = send_mail(email_title, email_boby, EMAIL_FROM, [email])
        if send_status:
            pass



def generate_random_str(randomlength=8):
    str = ''
    chars = 'QqWwEeRrTtYyUuIiOoPpAaSsDdFfGgHhJjKkLlZzXxCcVvBbNnMm0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str += chars[random.randint(0, length)]
    return str









