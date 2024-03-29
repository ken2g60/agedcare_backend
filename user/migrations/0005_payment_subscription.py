# Generated by Django 3.0 on 2020-06-16 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_customuser_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='First Name')),
                ('last_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Last Name')),
                ('phonenumber', models.CharField(blank=True, max_length=50, null=True, verbose_name='Phone Number')),
                ('subscription', models.CharField(max_length=50, verbose_name='Subscription Type')),
                ('paid_status', models.BooleanField(default=False, verbose_name='Payment Status')),
                ('paid_date', models.DateField(blank=True, null=True, verbose_name='Paid Date')),
                ('amount', models.CharField(max_length=50, verbose_name='Amount')),
                ('terminated_on', models.DateField(blank=True, null=True, verbose_name='Terminated Date')),
                ('email', models.CharField(blank=True, max_length=50, null=True, verbose_name='Email Address')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phonenumber', models.CharField(max_length=50, verbose_name='Phone Number')),
                ('subscription_type', models.CharField(choices=[('select option', 'select option'), ('monthly', 'monthly'), ('three_months', 'three_months'), ('six_months', 'six_months'), ('annual', 'annual')], max_length=50, verbose_name='Subscription Type')),
                ('is_active', models.BooleanField(default=False)),
                ('initiated_on', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
            ],
        ),
    ]
