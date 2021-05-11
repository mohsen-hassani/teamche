# Generated by Django 3.1.2 on 2021-05-11 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_auto_20210420_1154'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='accountsetting',
            options={'permissions': [('edit_setting', 'ویرایش تنظیمات')], 'verbose_name': 'تنظیمات حساب', 'verbose_name_plural': 'تنظیمات حساب'},
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'permissions': [('edit_permission', 'ویرایش کاربران یا گروه\u200cها'), ('view_user', 'مشاهده کاربران و پروفایل\u200cها'), ('add_user', 'ایجاد کاربران و پروفایل\u200cها'), ('edit_user', 'ویرایش کاربران و پروفایل\u200cها'), ('edit_user_pass', 'تغییر رمز کاربران'), ('delete_user', 'حذف کاربران و پروفایل\u200cها'), ('view_group', 'مشاهده گروه\u200cها و اعضا'), ('add_group', 'ایجاد گروه\u200cها'), ('edit_group', 'ویرایش گروه\u200cها'), ('group_membership', 'ویرایش اعضای گروه'), ('delete_group', 'حذف گروه\u200cها')], 'verbose_name': 'پروفایل', 'verbose_name_plural': 'پروفایل\u200cها'},
        ),
        migrations.RemoveField(
            model_name='profile',
            name='preferred_language',
        ),
        migrations.DeleteModel(
            name='UserAddress',
        ),
    ]
