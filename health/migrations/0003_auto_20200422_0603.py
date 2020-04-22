# Generated by Django 3.0 on 2020-04-22 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0002_auto_20200324_1150'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='glucose',
            name='userId',
        ),
        migrations.RemoveField(
            model_name='pressure',
            name='userId',
        ),
        migrations.RemoveField(
            model_name='weight',
            name='userId',
        ),
        migrations.AddField(
            model_name='glucose',
            name='username',
            field=models.CharField(default=True, max_length=50, verbose_name='UserName'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pressure',
            name='username',
            field=models.CharField(default=True, max_length=50, verbose_name='UserName'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='weight',
            name='username',
            field=models.CharField(default=True, max_length=50, verbose_name='UserName'),
            preserve_default=False,
        ),
    ]