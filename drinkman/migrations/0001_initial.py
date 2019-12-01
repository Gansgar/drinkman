# Generated by Django 2.2.7 on 2019-11-28 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('image', models.FilePathField()),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.TextField()),
                ('balance', models.IntegerField()),
                ('image_url', models.TextField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('message', models.TextField()),
                ('date', models.DateTimeField()),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='drinkman.Item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drinkman.User')),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drinkman.Item')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drinkman.Location')),
            ],
        ),
    ]