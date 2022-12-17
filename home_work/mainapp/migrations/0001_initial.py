# Generated by Django 3.2 on 2022-12-16 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='ФИО')),
                ('estimation', models.IntegerField(verbose_name='Оценка')),
                ('group', models.IntegerField(verbose_name='Номер группы')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Список студентов',
                'verbose_name_plural': 'Списки студентов',
                'ordering': ['-created_at'],
            },
        ),
    ]
