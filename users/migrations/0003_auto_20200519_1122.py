# Generated by Django 3.0.6 on 2020-05-19 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200515_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='immagine',
            field=models.ImageField(default='default.png', upload_to=''),
        ),
    ]
