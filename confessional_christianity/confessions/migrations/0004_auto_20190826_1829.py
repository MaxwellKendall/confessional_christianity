# Generated by Django 2.2.4 on 2019-08-26 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('confessions', '0003_auto_20190824_1847'),
    ]

    operations = [
        migrations.AddField(
            model_name='confessions',
            name='authors',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='confessions',
            name='location',
            field=models.TextField(blank=True, null=True),
        ),
    ]
