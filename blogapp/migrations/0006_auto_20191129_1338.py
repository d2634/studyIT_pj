# Generated by Django 2.2.7 on 2019-11-29 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0005_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='pub_date',
            field=models.CharField(max_length=100),
        ),
    ]
