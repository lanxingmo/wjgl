# Generated by Django 2.2.3 on 2019-11-06 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20191106_0923'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useroperatelog',
            name='content',
        ),
        migrations.RemoveField(
            model_name='useroperatelog',
            name='content_id',
        ),
        migrations.AddField(
            model_name='useroperatelog',
            name='filename',
            field=models.CharField(default='', max_length=200, verbose_name='文件名称'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='useroperatelog',
            name='fileno',
            field=models.CharField(default='', max_length=18, verbose_name='文件编号'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='role',
            field=models.CharField(choices=[('3', '监察稽核员'), ('2', '系统管理员'), ('1', '普通员工'), ('0', '离职员工')], default='1', max_length=1, verbose_name='用户角色'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='sub_role',
            field=models.CharField(choices=[('2', '二审员'), ('1', '初审员'), ('0', '')], default='0', max_length=1, verbose_name='子角色'),
        ),
    ]