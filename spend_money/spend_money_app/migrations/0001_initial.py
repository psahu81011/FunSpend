# Generated by Django 3.0.8 on 2020-07-25 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='products',
            fields=[
                ('name', models.CharField(max_length=128, unique=True)),
                ('price', models.IntegerField()),
                ('picture', models.ImageField(upload_to='product_img')),
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]
