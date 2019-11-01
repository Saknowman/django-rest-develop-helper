# Generated by Django 2.2.6 on 2019-11-01 03:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('columns', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ColumnType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_name', models.CharField(max_length=30)),
                ('value', models.CharField(max_length=40)),
            ],
        ),
        migrations.AddField(
            model_name='column',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='columns', to='columns.ColumnType'),
        ),
    ]
