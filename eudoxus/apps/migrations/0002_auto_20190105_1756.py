# Generated by Django 2.1.4 on 2019-01-05 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='semester',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]