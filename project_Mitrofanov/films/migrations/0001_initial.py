# Generated by Django 4.1.2 on 2022-12-20 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Films',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('date_made', models.DateField()),
                ('acteru', models.TextField()),
                ('date_show', models.DateField()),
            ],
        ),
    ]
