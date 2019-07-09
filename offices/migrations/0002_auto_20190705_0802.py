# Generated by Django 2.2.3 on 2019-07-05 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('offices', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name_plural': 'companies'},
        ),
        migrations.RemoveField(
            model_name='Office',
            name='headquarter',
        ),
        migrations.CreateModel(
            name='CompanyHeadquarter',
            fields=[
                ('company', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='offices.Company')),
                ('Office', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='offices.Office')),
            ],
        ),
    ]
