# Generated by Django 3.2 on 2022-04-26 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0015_serviceitem_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviceitem',
            name='in_home',
            field=models.BooleanField(default=False, verbose_name='In home page services section?'),
        ),
    ]