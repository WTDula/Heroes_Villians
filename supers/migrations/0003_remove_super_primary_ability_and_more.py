# Generated by Django 4.0.3 on 2022-04-05 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supers', '0002_power'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='super',
            name='primary_ability',
        ),
        migrations.RemoveField(
            model_name='super',
            name='secondary_ability',
        ),
        migrations.AddField(
            model_name='super',
            name='powers',
            field=models.ManyToManyField(to='supers.power'),
        ),
    ]