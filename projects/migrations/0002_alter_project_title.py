# Generated by Django 4.0.3 on 2022-03-15 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]
