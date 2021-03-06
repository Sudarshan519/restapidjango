# Generated by Django 3.1.7 on 2021-04-03 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hero',
            name='description',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='hero',
            name='image',
            field=models.ImageField(default='', upload_to='myapi/images'),
        ),
        migrations.AddField(
            model_name='hero',
            name='task_priority',
            field=models.CharField(default=1, max_length=100),
        ),
    ]
