# Generated by Django 3.0.5 on 2020-04-23 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edc_data_manager', '0003_auto_20200423_1404'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataactionitem',
            name='subject',
            field=models.CharField(default='', max_length=100, verbose_name='Issue Subject'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dataactionitem',
            name='assign',
            field=models.CharField(blank=True, choices=[], max_length=50, null=True, verbose_name='Assign to'),
        ),
    ]
