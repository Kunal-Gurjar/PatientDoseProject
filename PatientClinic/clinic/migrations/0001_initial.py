# Generated by Django 4.1.7 on 2023-02-23 07:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('machine_id', models.IntegerField(editable=False, primary_key=True, serialize=False)),
                ('machine_name', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('patient_id', models.IntegerField(editable=False, primary_key=True, serialize=False)),
                ('patient_name', models.CharField(max_length=50)),
                ('machine_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinic.machine')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Dose',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('dose_id', models.AutoField(primary_key=True, serialize=False)),
                ('dose', models.FloatField()),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinic.patient')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
