# Generated by Django 2.1.7 on 2019-03-15 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_catagory_event_news'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='catagory',
        ),
        migrations.AddField(
            model_name='news',
            name='catagory',
            field=models.ManyToManyField(to='blogapp.Catagory'),
        ),
    ]
