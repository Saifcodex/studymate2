# Generated by Django 5.1.7 on 2025-04-01 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_remove_chaptertutor_preferred_classes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generalappointment',
            name='class_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
