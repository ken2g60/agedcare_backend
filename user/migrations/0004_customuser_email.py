# Generated by Django 3.0 on 2020-04-25 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_customuser_userid'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='email',
            field=models.CharField(default=True, max_length=50, verbose_name='Email Address'),
            preserve_default=False,
        ),
    ]
