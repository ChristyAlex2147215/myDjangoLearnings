# Generated by Django 4.0.4 on 2022-05-21 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=15)),
                ('lname', models.CharField(max_length=15)),
                ('dob', models.DateField()),
                ('password', models.CharField(max_length=15)),
            ],
        ),
    ]
