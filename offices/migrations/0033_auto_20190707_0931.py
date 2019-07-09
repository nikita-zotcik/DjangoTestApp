# Generated by Django 2.2.3 on 2019-07-07 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('offices', '0032_auto_20190706_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='headquarter',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='is_headquarter', to='offices.Office'),
        ),
        migrations.AlterField(
            model_name='Office',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='offices', to='offices.Company'),
        ),
    ]
