# Generated by Django 4.1.3 on 2022-12-06 01:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='project_tasks', to='webapp.project', verbose_name='Проект'),
            preserve_default=False,
        ),
    ]
