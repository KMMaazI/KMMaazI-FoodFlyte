# Generated by Django 5.1.2 on 2024-11-26 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_orders'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='price',
            field=models.DecimalField(decimal_places=2, default=100, max_digits=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orders',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
