# Generated by Django 4.2.6 on 2023-12-07 23:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enquetes', '0006_remove_opcaoresposta_quantidade_votada'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pergunta',
            name='total_respostas',
        ),
    ]
