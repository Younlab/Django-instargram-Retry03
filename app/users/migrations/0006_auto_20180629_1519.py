# Generated by Django 2.0.6 on 2018-06-29 06:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20180629_1434'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='relation',
            unique_together={('from_user', 'to_user')},
        ),
    ]
