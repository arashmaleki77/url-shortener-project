# Generated by Django 4.2.3 on 2023-07-14 18:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0002_remove_shortener_favorite_link'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shortener',
            old_name='count',
            new_name='click_count',
        ),
    ]
