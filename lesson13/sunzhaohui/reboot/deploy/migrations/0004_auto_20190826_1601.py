# Generated by Django 2.2 on 2019-08-26 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deploy', '0003_auto_20190826_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deploy',
            name='status',
            field=models.IntegerField(choices=[(0, '申请'), (1, '审核'), (2, '上线'), (3, '已取消'), (4, '已上线'), (5, '失败')], default=0, verbose_name='上线状态'),
        ),
    ]
