# Generated by Django 3.2.5 on 2021-09-21 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20210921_0940'),
    ]

    operations = [
        migrations.AddField(
            model_name='texts',
            name='view_id',
            field=models.CharField(default=0, max_length=20, unique=True),
        ),
    ]
