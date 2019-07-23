# Generated by Django 2.2 on 2019-07-21 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('phone', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name': 'users',
                'verbose_name_plural': 'users',
                'db_table': 'users',
            },
        ),
    ]
