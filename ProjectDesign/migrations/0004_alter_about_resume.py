# Generated by Django 3.2.5 on 2023-05-04 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectDesign', '0003_about_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='resume',
            field=models.FileField(default='default.pdf', upload_to='About/'),
        ),
    ]
