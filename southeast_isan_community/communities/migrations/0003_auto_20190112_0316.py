# Generated by Django 2.1.5 on 2019-01-12 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0002_auto_20190112_0314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='faith',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='community',
            name='folk_game',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='community',
            name='regional_dialect',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
