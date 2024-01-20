# Generated by Django 4.1.4 on 2024-01-17 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_alter_patient_patient_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='uploads/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('is_annotated', models.BooleanField(default=False)),
                ('temperature_data', models.JSONField(blank=True, null=True)),
            ],
        ),
    ]