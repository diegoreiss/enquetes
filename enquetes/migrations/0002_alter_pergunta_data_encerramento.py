# Generated by Django 5.0 on 2023-12-06 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enquetes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pergunta',
            name='data_encerramento',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]