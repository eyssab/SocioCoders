# Generated by Django 5.0.4 on 2024-04-25 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sim', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='classes',
            field=models.ManyToManyField(blank=True, related_name='students', to='sim.class'),
        ),
    ]