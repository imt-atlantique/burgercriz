# Generated by Django 3.2.5 on 2022-12-23 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0006_alter_card_public'),
    ]

    operations = [
        migrations.AddField(
            model_name='deck',
            name='public',
            field=models.BooleanField(default=True, verbose_name='Paquet public ?'),
        ),
    ]
