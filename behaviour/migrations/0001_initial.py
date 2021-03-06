# Generated by Django 3.0.2 on 2020-01-31 18:39

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
            name='BehaviourReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('report', models.TextField(max_length=2000)),
                ('public_outcome', models.CharField(blank=True, max_length=255)),
                ('private_outcome', models.CharField(blank=True, max_length=255)),
                ('status', models.CharField(choices=[('not_reviewed', 'Not reviewed'), ('under_review', 'Under review'), ('completed', 'Completed')], default='not_reviewed', max_length=50)),
                ('reportee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reportee', to=settings.AUTH_USER_MODEL)),
                ('reporter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reporter', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-modified'],
            },
        ),
    ]
