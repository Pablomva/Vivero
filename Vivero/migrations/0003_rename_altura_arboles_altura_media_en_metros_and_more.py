# Generated by Django 4.0.4 on 2022-05-28 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Vivero', '0002_rename_altura_arbustos_altura_media_en_metros'),
    ]

    operations = [
        migrations.RenameField(
            model_name='arboles',
            old_name='altura',
            new_name='altura_media_en_metros',
        ),
        migrations.RenameField(
            model_name='herbaceas',
            old_name='altura',
            new_name='altura_media_en_metros',
        ),
    ]
