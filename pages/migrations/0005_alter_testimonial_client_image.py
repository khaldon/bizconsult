# Generated by Django 4.1.1 on 2022-09-10 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_testimonial_client_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='client_image',
            field=models.ImageField(upload_to='images'),
        ),
    ]
