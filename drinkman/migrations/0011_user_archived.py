# Generated by Django 3.1.2 on 2020-10-19 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drinkman', '0010_auto_20201017_1032'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='archived',
            field=models.BooleanField(default=0),
        ),
    ]
