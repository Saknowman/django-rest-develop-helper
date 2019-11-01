# Generated by Django 2.2.6 on 2019-11-01 06:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('columns', '0004_auto_20191101_1348'),
    ]

    operations = [
        migrations.CreateModel(
            name='ColumnOptionType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_name', models.CharField(max_length=80, unique=True)),
                ('value', models.CharField(max_length=80, unique=True)),
                ('detail', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='ColumnTypeAndOptionTypeRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('required', models.BooleanField(default=False)),
                ('column_type', models.ForeignKey(on_delete=django.db.models.CASCADE, to='columns.ColumnType')),
                ('option_type', models.ForeignKey(on_delete=django.db.models.CASCADE, to='columns.ColumnOptionType')),
            ],
        ),
        migrations.DeleteModel(
            name='ColumnOptionTypes',
        ),
        migrations.AddField(
            model_name='columntype',
            name='options_type',
            field=models.ManyToManyField(through='columns.ColumnTypeAndOptionTypeRelation', to='columns.ColumnOptionType'),
        ),
    ]
