# Generated by Django 3.0 on 2020-10-09 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RouterModel',
            fields=[
                ('idno', models.AutoField(primary_key=True, serialize=False)),
                ('router_name', models.CharField(max_length=30)),
            ],
        ),
    ]
