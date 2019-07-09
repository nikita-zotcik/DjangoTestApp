# Generated by Django 2.2.3 on 2019-07-06 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('offices', '0031_auto_20190706_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='headquarter',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='is_headquarter', to='offices.Office'),
        ),
    ]
