# Generated by Django 3.0.2 on 2020-01-19 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('hashtag', models.CharField(max_length=40)),
                ('collective_noun', models.CharField(default='attendees', max_length=40)),
                ('polling_interval', models.PositiveSmallIntegerField(default=5)),
                ('location', models.CharField(blank=True, max_length=255)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('link', models.URLField(blank=True)),
                ('coc_link', models.URLField(blank=True)),
                ('message', models.TextField(blank=True, max_length=500)),
            ],
        ),
    ]
