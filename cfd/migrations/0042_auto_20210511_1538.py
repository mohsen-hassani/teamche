# Generated by Django 3.1.2 on 2021-05-11 11:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
        ('cfd', '0041_auto_20210420_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ptaanalysis',
            name='news_detail',
            field=models.TextField(blank=True, help_text='توجه: سی دقیقه قبل و بعد از خبر نباید وارد معامله شوید، اما در صورتی که برای انجام معامله مصر هستید، اطلاعات خبر را اینجا وارد کنید.', null=True, verbose_name='جزئیات خبر'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_on', models.DateTimeField(auto_now=True, verbose_name='تاریخ')),
                ('body', models.CharField(max_length=500, verbose_name='متن نظر')),
                ('public', models.BooleanField(default=True, verbose_name='عمومی')),
                ('object_id', models.PositiveIntegerField(blank=True, null=True)),
                ('content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'نظر',
                'verbose_name_plural': 'نظرات',
            },
        ),
    ]
