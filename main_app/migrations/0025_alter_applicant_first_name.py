# Generated by Django 3.2.6 on 2021-08-30 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0024_alter_applicant_first_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='first_name',
            field=models.CharField(blank=True, default='Kevin', max_length=35),
            preserve_default=False,
        ),
    ]