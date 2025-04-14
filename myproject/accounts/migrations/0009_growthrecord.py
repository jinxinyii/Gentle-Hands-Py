# Generated by Django 5.0.4 on 2025-04-14 14:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_immunization'),
    ]

    operations = [
        migrations.CreateModel(
            name='GrowthRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.PositiveIntegerField()),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5)),
                ('height', models.DecimalField(decimal_places=2, max_digits=5)),
                ('head_circumference', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('chest_circumference', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('teeth_upper', models.PositiveIntegerField(blank=True, null=True)),
                ('teeth_lower', models.PositiveIntegerField(blank=True, null=True)),
                ('date_recorded', models.DateField(auto_now_add=True)),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.child')),
            ],
        ),
    ]
