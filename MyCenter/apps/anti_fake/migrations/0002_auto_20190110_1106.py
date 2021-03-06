# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-10 03:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
        ('anti_fake', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='realtime',
            options={'verbose_name': '实时数据', 'verbose_name_plural': '实时数据'},
        ),
        migrations.RemoveField(
            model_name='realtime',
            name='category',
        ),
        migrations.RemoveField(
            model_name='realtime',
            name='real_company',
        ),
        migrations.RemoveField(
            model_name='realtime',
            name='real_time',
        ),
        migrations.AddField(
            model_name='realtime',
            name='r_product',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='product.Product', verbose_name='产品类别'),
        ),
        migrations.AlterField(
            model_name='realtime',
            name='logistics',
            field=models.CharField(max_length=20, verbose_name='物流码'),
        ),
        migrations.AlterField(
            model_name='realtime',
            name='query_id',
            field=models.CharField(max_length=20, verbose_name='查询id'),
        ),
    ]
