# Generated by Django 5.0.4 on 2024-05-14 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_rest', '0005_alter_user_createdat_alter_user_updatedat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='itens',
        ),
    ]
