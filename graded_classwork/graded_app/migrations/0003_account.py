# Generated by Django 2.0.6 on 2019-09-24 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graded_app', '0002_auto_20190924_1618'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=15)),
                ('realName', models.CharField(max_length=50)),
                ('accountNumber', models.IntegerField()),
                ('balance', models.IntegerField()),
            ],
        ),
    ]
