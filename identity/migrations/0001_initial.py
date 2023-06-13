# Generated by Django 3.2.9 on 2022-12-06 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_no', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'person',
            },
        ),
    ]
