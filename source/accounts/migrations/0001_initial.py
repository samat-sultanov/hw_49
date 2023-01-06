# Generated by Django 4.1.3 on 2022-12-26 16:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_github', models.URLField(blank=True, null=True, verbose_name='Ссылка на профиль GitHub')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='user_avatar', verbose_name='Аватар')),
                ('about', models.TextField(blank=True, max_length=200, null=True, verbose_name='О себе')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили',
                'db_table': 'profile',
            },
        ),
    ]