# Generated by Django 2.2.9 on 2019-12-30 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customtext',
            name='test',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
