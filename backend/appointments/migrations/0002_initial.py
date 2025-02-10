# Generated by Django 5.1.4 on 2025-02-10 13:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('appointments', '0001_initial'),
        ('pets', '0001_initial'),
        ('services', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_appointments', to='users.user'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='pet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pets.pet'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='worker',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='worker_appointments', to='users.user'),
        ),
        migrations.AddField(
            model_name='appointmentservice',
            name='appointment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointments.appointment'),
        ),
        migrations.AddField(
            model_name='appointmentservice',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.service'),
        ),
    ]
