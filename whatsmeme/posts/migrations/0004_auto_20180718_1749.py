# Generated by Django 2.2 on 2018-07-18 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20180718_1742'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-commented_at']},
        ),
    ]