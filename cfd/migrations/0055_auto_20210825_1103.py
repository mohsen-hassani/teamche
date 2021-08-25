# Generated by Django 3.1.2 on 2021-08-25 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cfd', '0054_auto_20210810_2318'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='signalevent',
            options={'ordering': ['event_datetime'], 'verbose_name': 'رخداد سیگنال', 'verbose_name_plural': 'رخدادهای سیگنال'},
        ),
        migrations.AddField(
            model_name='ptaanalysis',
            name='title',
            field=models.CharField(max_length=100, null=True, verbose_name='عنوان'),
        ),
        migrations.AlterField(
            model_name='classicanalysis',
            name='image_url',
            field=models.URLField(max_length=300, null=True, verbose_name='URL تصویر'),
        ),
        migrations.AlterField(
            model_name='ptaanalysis',
            name='image_url',
            field=models.URLField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='signal',
            name='result_image_url',
            field=models.URLField(max_length=300, null=True, verbose_name='تصویر نهایی'),
        ),
        migrations.AlterField(
            model_name='signal',
            name='status',
            field=models.CharField(choices=[('pending', 'باز نشده'), ('running', 'در حال اجرا'), ('filled', 'انجام شده'), ('canceled', 'لغو شده')], default='pending', max_length=8, verbose_name='وضعیت'),
        ),
        migrations.AlterField(
            model_name='signalevent',
            name='event_type',
            field=models.CharField(choices=[('open', 'باز کردن سیگنال'), ('close', 'بستن'), ('cancel', 'لغو سیگنال'), ('change_sl', 'تغییر حد ضرر'), ('change_tp', 'تغییر حد سود'), ('dec_lot', 'کاهش حجم'), ('inc_lot', 'افزایش حجم')], default='open', max_length=10, verbose_name='نوع رخداد'),
        ),
    ]
