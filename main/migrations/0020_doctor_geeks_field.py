# Generated by Django 4.1.4 on 2024-01-17 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='geeks_field',
            field=models.CharField(blank=True, choices=[('Operator', 'Operator'), ('Doctor', 'Doctor')], max_length=10, null=True),
        ),
    ]