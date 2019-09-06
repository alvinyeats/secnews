# Generated by Django 2.2.5 on 2019-09-03 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CVE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cve_id', models.CharField(max_length=20, unique=True, verbose_name='CVE编号')),
                ('description', models.TextField(verbose_name='漏洞描述')),
                ('keyword', models.CharField(default='', max_length=100, verbose_name='关键字')),
                ('created', models.DateField(verbose_name='创建时间')),
                ('updated', models.DateField(auto_now=True, verbose_name='更新时间')),
                ('origin', models.URLField(verbose_name='源地址')),
            ],
            options={
                'verbose_name': 'CVE',
                'verbose_name_plural': 'CVE',
                'ordering': ['-updated'],
            },
        ),
        migrations.CreateModel(
            name='VulCNNVD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='漏洞名称')),
                ('cnnvd_id', models.CharField(max_length=20, unique=True, verbose_name='CNNVD编号')),
                ('cve_id', models.CharField(max_length=20, unique=True, verbose_name='CVE编号')),
                ('description', models.TextField(verbose_name='漏洞描述')),
                ('keyword', models.CharField(default='', max_length=100, verbose_name='关键字')),
                ('created', models.DateField(verbose_name='创建时间')),
                ('updated', models.DateField(auto_now=True, verbose_name='更新时间')),
                ('origin', models.URLField(verbose_name='源地址')),
            ],
            options={
                'verbose_name': 'CNNVD',
                'verbose_name_plural': 'CNNVD',
                'ordering': ['-updated'],
            },
        ),
        migrations.CreateModel(
            name='VulPaper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True, verbose_name='标题')),
                ('tag', models.CharField(default='', max_length=100, verbose_name='标签')),
                ('content', models.TextField(verbose_name='内容')),
                ('website', models.CharField(max_length=20, verbose_name='站点名称')),
                ('created', models.DateField(verbose_name='创建时间')),
                ('updated', models.DateField(auto_now=True, verbose_name='更新时间')),
                ('origin', models.URLField(verbose_name='源地址')),
            ],
            options={
                'verbose_name': 'Paper',
                'verbose_name_plural': 'Paper',
                'ordering': ['-updated'],
            },
        ),
    ]