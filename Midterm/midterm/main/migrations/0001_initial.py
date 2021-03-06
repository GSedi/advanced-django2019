# Generated by Django 2.1.1 on 2019-10-15 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=21)),
                ('description', models.TextField(max_length=500)),
                ('price', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('size', models.IntegerField()),
                ('type', models.PositiveSmallIntegerField(choices=[(1, 'one'), (2, 'two'), (3, 'three')], default=1)),
                ('existence', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=21)),
                ('description', models.TextField(max_length=500)),
                ('price', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('approximate_duration', models.PositiveIntegerField()),
                ('service_type', models.PositiveSmallIntegerField(choices=[(1, 'one'), (2, 'two'), (3, 'three')], default=1)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
