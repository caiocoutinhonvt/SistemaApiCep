# Generated by Django 4.0.5 on 2022-06-25 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_descrição_adress_descricao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adress',
            name='uf',
            field=models.CharField(max_length=2),
        ),
    ]
