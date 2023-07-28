# Generated by Django 4.2.1 on 2023-07-27 10:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('dob', models.DateField(auto_now=True)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=250, unique=True)),
                ('number', models.IntegerField()),
                ('mail', models.CharField(max_length=250, unique=True)),
                ('address', models.TextField(blank=True)),
                ('district', models.CharField(max_length=250, unique=True)),
                ('account', models.CharField(max_length=250, unique=True)),
            ],
            options={
                'verbose_name': 'form',
                'verbose_name_plural': 'forms',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Dropdown',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.CharField(max_length=250, unique=True)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankingapp.form')),
            ],
            options={
                'verbose_name': 'dropdown',
                'verbose_name_plural': 'dropdowns',
                'ordering': ('district',),
            },
        ),
        migrations.CreateModel(
            name='Dependent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('credit', models.BooleanField(default=True)),
                ('debit', models.BooleanField(default=True)),
                ('cheque', models.BooleanField(default=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankingapp.form')),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankingapp.dropdown')),
            ],
            options={
                'verbose_name': 'dependent',
                'verbose_name_plural': 'dependents',
                'ordering': ('branch',),
            },
        ),
    ]