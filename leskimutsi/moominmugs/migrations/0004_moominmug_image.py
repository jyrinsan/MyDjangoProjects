# Generated by Django 5.0 on 2023-12-11 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moominmugs', '0003_moominmug_officialname'),
    ]

    operations = [
        migrations.AddField(
            model_name='moominmug',
            name='image',
            field=models.ImageField(default='', upload_to='images/'),
            preserve_default=False,
        ),
    ]
