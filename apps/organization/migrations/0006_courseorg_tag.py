# Generated by Django 2.0.3 on 2018-03-25 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0005_teacher_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseorg',
            name='tag',
            field=models.CharField(default='全国知名', max_length=20, verbose_name='机构标签'),
        ),
    ]
