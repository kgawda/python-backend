# Generated by Django 4.0.3 on 2022-05-22 13:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('buildingmanagement', '0012_projector'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('rooms', models.ManyToManyField(to='buildingmanagement.room')),
            ],
        ),
    ]
