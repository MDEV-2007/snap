# Generated by Django 4.2.5 on 2023-10-02 16:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_alter_follow_follow_alter_follow_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follow',
            name='follow',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followers', to=settings.AUTH_USER_MODEL),
        ),
    ]