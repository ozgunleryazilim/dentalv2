# Generated by Django 3.2 on 2022-04-03 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0003_servicecategory_servicecategorytranslation'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicecategory',
            name='in_home',
            field=models.BooleanField(default=False, verbose_name='In home page services section?'),
        ),
    ]
