# Generated by Django 2.2.6 on 2019-11-01 02:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ColumnOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=80)),
                ('value', models.CharField(max_length=80)),
                ('column', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='columns.Column')),
            ],
        ),
    ]
