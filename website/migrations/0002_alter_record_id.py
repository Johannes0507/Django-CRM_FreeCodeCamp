# Generated by Django 5.0 on 2024-01-01 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='id',
            field=models.CharField(editable=False, max_length=20, primary_key=True, serialize=False),
        ),
    ]
