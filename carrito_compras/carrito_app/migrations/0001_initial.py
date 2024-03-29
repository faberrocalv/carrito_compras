# Generated by Django 5.0.3 on 2024-03-08 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=50)),
                ('cantidad_disponible', models.FloatField()),
                ('precio_unitario', models.FloatField()),
            ],
            options={
                'db_table': 'producto',
                'managed': True,
            },
        ),
    ]
