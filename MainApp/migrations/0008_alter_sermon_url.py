# Generated by Django 5.0.4 on 2024-04-16 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0007_activity_image_alter_department_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sermon',
            name='url',
            field=models.TextField(blank=True, null=True),
        ),
    ]
