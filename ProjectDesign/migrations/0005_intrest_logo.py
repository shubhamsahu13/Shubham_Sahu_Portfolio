# Generated by Django 3.2.5 on 2023-05-04 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectDesign', '0004_alter_about_resume'),
    ]

    operations = [
        migrations.AddField(
            model_name='intrest',
            name='logo',
            field=models.CharField(default='Some logo', max_length=255),
        ),
    ]
