# Generated by Django 2.0.3 on 2018-03-20 20:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_course_course_org'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='category',
            field=models.CharField(default='后端开发', max_length=20, verbose_name='章节类别'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course', verbose_name='课程'),
        ),
    ]