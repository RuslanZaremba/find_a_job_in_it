# Generated by Django 3.2.6 on 2021-09-16 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_work', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'ordering': ['pk'], 'verbose_name': 'Компания', 'verbose_name_plural': 'Компании'},
        ),
        migrations.AlterModelOptions(
            name='specialty',
            options={'ordering': ['pk'], 'verbose_name': 'Специализация', 'verbose_name_plural': 'Специализации'},
        ),
        migrations.AlterModelOptions(
            name='vacancy',
            options={'ordering': ['-published_at'], 'verbose_name': 'Вакансия', 'verbose_name_plural': 'Вакансии'},
        ),
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.ImageField(upload_to='companies_logo/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='specialty',
            name='picture',
            field=models.ImageField(upload_to='specialties/'),
        ),
    ]
