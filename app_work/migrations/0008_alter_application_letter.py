# Generated by Django 3.2.6 on 2021-09-30 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_work', '0007_alter_application_letter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='letter',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
