# Generated by Django 3.0 on 2020-03-24 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('careapp', '0005_auto_20200324_1150'),
        ('health', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Glucose',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.CharField(max_length=50, verbose_name='User ID')),
                ('glucose', models.CharField(max_length=50, verbose_name='Glucose')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Created At')),
            ],
        ),
        migrations.CreateModel(
            name='Pressure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.CharField(max_length=50, verbose_name='User ID')),
                ('systolic', models.CharField(max_length=50, verbose_name='Systolic')),
                ('diastolic', models.CharField(max_length=50, verbose_name='Diastolic')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Created At')),
            ],
        ),
        migrations.CreateModel(
            name='Weight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.CharField(max_length=50, verbose_name='User ID')),
                ('weight', models.CharField(max_length=50, verbose_name='Weight')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Created At')),
            ],
        ),
        migrations.AddField(
            model_name='healthdata',
            name='user',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='careapp.UserModel'),
            preserve_default=False,
        ),
    ]
