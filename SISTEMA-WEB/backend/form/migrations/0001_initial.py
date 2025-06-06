# Generated by Django 5.2 on 2025-05-15 01:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AyudaTecnica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='DataEntrega',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('resident', models.CharField(max_length=10)),
                ('identification', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=20)),
                ('diagnostic', models.CharField(blank=True, max_length=100, null=True)),
                ('age', models.CharField(blank=True, max_length=10, null=True)),
                ('direction', models.TextField()),
                ('observation', models.TextField(blank=True, null=True)),
                ('state', models.CharField(max_length=100)),
                ('municipality', models.CharField(max_length=100)),
                ('parish', models.CharField(max_length=100)),
                ('identificationRefererPerson', models.IntegerField(blank=True, null=True)),
                ('nameRefererPerson', models.CharField(blank=True, max_length=100, null=True)),
                ('nameRefererOrganization', models.CharField(blank=True, max_length=100, null=True)),
                ('identificationRefererOrganization', models.IntegerField(blank=True, null=True)),
                ('identificationRefererAssociation', models.IntegerField(blank=True, null=True)),
                ('nameRefererAssociation', models.CharField(blank=True, max_length=100, null=True)),
                ('applicant_active', models.BooleanField(default=False)),
                ('main', models.TextField(blank=True, null=True)),
                ('recipes', models.TextField(blank=True, null=True)),
                ('archivo_adjunto', models.FileField(blank=True, null=True, upload_to='adjuntos/')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('nameApplicant', models.CharField(blank=True, max_length=128, null=True)),
                ('lastnameApplicant', models.CharField(blank=True, max_length=128, null=True)),
                ('residentApplicant', models.CharField(blank=True, max_length=10, null=True)),
                ('identificationApplicant', models.CharField(blank=True, max_length=20, null=True)),
                ('phoneApplicant', models.CharField(blank=True, max_length=20, null=True)),
                ('ageApplicant', models.CharField(blank=True, max_length=10, null=True)),
                ('status', models.CharField(choices=[('PENDIENTE', 'Pendiente'), ('EN_REVISION', 'En Revisión'), ('APROBADO', 'Aprobado'), ('RECHAZADO', 'Rechazado'), ('ENTREGADO', 'Entregado')], default='PENDIENTE', help_text='Estado actual de la solicitud', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ItemEntregado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
                ('ayuda_tecnica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form.ayudatecnica')),
                ('data_entrega', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='form.dataentrega')),
            ],
        ),
    ]
