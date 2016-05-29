# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-23 12:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30, verbose_name='nome')),
                ('foto', models.ImageField(blank=True, default='cliente/no_foto.jpg', null=True, upload_to='cliente/')),
            ],
            managers=[
                ('cliente', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField(default=0, verbose_name='numero')),
                ('tipo', models.IntegerField(default=0, verbose_name='tipo')),
                ('emissao', models.DateField(verbose_name='emissao')),
                ('vencimento', models.DateField(verbose_name='vencimennto')),
                ('ativo', models.IntegerField(default=0, verbose_name='ativo')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Cliente')),
            ],
            managers=[
                ('documento', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=30, verbose_name='email')),
                ('ativo', models.IntegerField(default=0, verbose_name='ativo')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cep', models.CharField(max_length=30, verbose_name='cep')),
                ('tipo', models.IntegerField(default=0, verbose_name='tipo')),
                ('descricao', models.CharField(max_length=30, verbose_name='descricao')),
                ('complemento', models.CharField(max_length=30, verbose_name='complemento')),
                ('numero', models.IntegerField(default=0, verbose_name='numero')),
                ('ativo', models.IntegerField(default=0, verbose_name='ativo')),
                ('documento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Documento')),
            ],
            managers=[
                ('endereco', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30, verbose_name='nome')),
                ('documento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Documento')),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Email')),
                ('endereco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Endereco')),
            ],
            managers=[
                ('fornecedor', django.db.models.manager.Manager()),
            ],
        ),
    ]
