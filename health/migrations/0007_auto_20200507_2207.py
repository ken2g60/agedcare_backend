# Generated by Django 3.0 on 2020-05-07 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0006_auto_20200507_1000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='glucose',
            name='glucose',
            field=models.CharField(max_length=50, verbose_name='Glucose'),
        ),
        migrations.AlterField(
            model_name='healthdata',
            name='weight',
            field=models.CharField(max_length=50, verbose_name='Weight'),
        ),
        migrations.AlterField(
            model_name='weight',
            name='weight',
            field=models.CharField(max_length=50, verbose_name='Weight'),
        ),
    ]