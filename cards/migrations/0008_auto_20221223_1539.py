# Generated by Django 3.2.5 on 2022-12-23 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0007_deck_public'),
    ]

    operations = [
        migrations.RenameField(
            model_name='card',
            old_name='card_text',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='card',
            old_name='card_text_rendered',
            new_name='text_rendered',
        ),
    ]