# Generated by Django 3.1 on 2020-09-07 20:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('painelInformacoes', '0002_painelinformacoes_usuario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='painelinformacoes',
            old_name='usuario',
            new_name='user',
        ),
    ]