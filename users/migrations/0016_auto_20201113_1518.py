# Generated by Django 3.0.8 on 2020-11-13 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_auto_20201113_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(default=0, max_length=5),
        ),
        migrations.AlterField(
            model_name='profile',
            name='favorite_food',
            field=models.TextField(default=0, max_length=5),
        ),
        migrations.AlterField(
            model_name='profile',
            name='favorite_hobby',
            field=models.TextField(default=0, max_length=5),
        ),
    ]
