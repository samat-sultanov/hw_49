# Generated by Django 4.1.3 on 2022-12-23 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_project_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'permissions': [('add_user_project', 'Добавить пользователя в проект'), ('remove_user_project', 'Удалить пользователя из проекта')], 'verbose_name': 'Проект', 'verbose_name_plural': 'Проекты'},
        ),
    ]
