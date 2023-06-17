# Generated by Django 4.2.2 on 2023-06-16 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FormConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campo', models.CharField(max_length=100)),
                ('exibir', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Proposta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Data atualização')),
                ('cpf', models.CharField(max_length=11)),
                ('nome', models.CharField(max_length=100)),
                ('status', models.IntegerField(choices=[(1, 'Análise Manual'), (2, 'Aprovado'), (3, 'Negado')], default=1)),
                ('finalizada', models.BooleanField(default=False)),
            ],
        ),
    ]