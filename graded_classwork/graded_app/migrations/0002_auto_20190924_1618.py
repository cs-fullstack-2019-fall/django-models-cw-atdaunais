# Generated by Django 2.0.6 on 2019-09-24 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graded_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('breed', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
