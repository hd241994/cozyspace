# Generated by Django 2.2 on 2021-10-29 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='getqoute',
            name='crockeryunit',
            field=models.IntegerField(max_length=10),
        ),
        migrations.AlterField(
            model_name='getqoute',
            name='entertainmentunit',
            field=models.IntegerField(max_length=10),
        ),
        migrations.AlterField(
            model_name='getqoute',
            name='kitchen',
            field=models.IntegerField(max_length=10),
        ),
        migrations.AlterField(
            model_name='getqoute',
            name='poojaroom',
            field=models.IntegerField(max_length=10),
        ),
        migrations.AlterField(
            model_name='getqoute',
            name='studyunit',
            field=models.IntegerField(max_length=10),
        ),
        migrations.AlterField(
            model_name='getqoute',
            name='wardrobe',
            field=models.IntegerField(max_length=10),
        ),
        migrations.AlterField(
            model_name='getqoute',
            name='washroom',
            field=models.IntegerField(max_length=10),
        ),
    ]
