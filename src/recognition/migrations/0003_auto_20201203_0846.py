# Generated by Django 3.0.8 on 2020-12-03 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recognition', '0002_faceimage_file_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userimageset',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
