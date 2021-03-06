# Generated by Django 2.2 on 2021-11-07 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20211107_0001'),
    ]

    operations = [
        migrations.AddField(
            model_name='getqoute',
            name='washroom',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='getqoute',
            name='crockeryunit',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='getqoute',
            name='entertainmentunit',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='getqoute',
            name='kitchen',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='getqoute',
            name='poojaroom',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='getqoute',
            name='studyunit',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='getqoute',
            name='wardrobe',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
