# Generated by Django 2.0.13 on 2019-04-14 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canteen_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodtype',
            name='image',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=12),
        ),
    ]
