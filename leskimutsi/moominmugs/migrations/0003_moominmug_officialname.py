# Generated by Django 5.0 on 2023-12-11 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moominmugs', '0002_moominmug_color_moominmug_figure_moominmug_theme_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='moominmug',
            name='officialName',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
