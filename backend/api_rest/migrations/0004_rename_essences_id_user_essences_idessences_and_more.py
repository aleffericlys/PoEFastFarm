# Generated by Django 5.0.4 on 2024-05-14 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_rest', '0003_rename_essences_idessences_user_essences_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='Essences_id',
            new_name='Essences_idEssences',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='Scarabs_id',
            new_name='Scarabs_idScarabs',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='oils_id',
            new_name='oils_oil_id',
        ),
    ]
