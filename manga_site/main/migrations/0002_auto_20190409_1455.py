# Generated by Django 2.2 on 2019-04-09 11:55

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pics',
            name='pic',
            field=models.ImageField(upload_to=main.models.get_image_filename),
        ),
    ]