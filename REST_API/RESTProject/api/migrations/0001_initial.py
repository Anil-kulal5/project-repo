# Generated by Django 4.1.6 on 2023-03-13 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('customer_name', models.CharField(max_length=50, verbose_name='name')),
                ('customer_address', models.TextField()),
                ('customer_contact', models.BigIntegerField()),
            ],
        ),
    ]
