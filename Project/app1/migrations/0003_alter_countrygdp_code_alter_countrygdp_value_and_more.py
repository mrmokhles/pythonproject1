# Generated by Django 5.0.3 on 2024-04-01 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_countrygdp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='countrygdp',
            name='code',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='countrygdp',
            name='value',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='countrygdp',
            name='year',
            field=models.CharField(max_length=5),
        ),
    ]
