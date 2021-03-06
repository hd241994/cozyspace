# Generated by Django 2.2 on 2021-10-29 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GetQoute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=100)),
                ('customer_email', models.EmailField(max_length=254)),
                ('customer_number', models.IntegerField(max_length=10)),
                ('possesion_time', models.CharField(max_length=20)),
                ('pincode', models.CharField(max_length=6)),
                ('floorPlan', models.CharField(max_length=100)),
                ('purpose', models.CharField(max_length=100)),
                ('kitchen', models.IntegerField()),
                ('wardrobe', models.IntegerField()),
                ('crockeryunit', models.IntegerField()),
                ('poojaroom', models.IntegerField()),
                ('studyunit', models.IntegerField()),
                ('entertainmentunit', models.IntegerField()),
                ('washroom', models.IntegerField()),
            ],
        ),
    ]
