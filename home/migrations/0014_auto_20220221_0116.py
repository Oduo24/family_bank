# Generated by Django 3.1.7 on 2022-02-20 22:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20220220_1102'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HandDryer',
            new_name='FlowMeter',
        ),
        migrations.RenameModel(
            old_name='Floodlight',
            new_name='Lights',
        ),
        migrations.RenameModel(
            old_name='Photocopier',
            new_name='Pumps',
        ),
        migrations.DeleteModel(
            name='Amplifier',
        ),
        migrations.DeleteModel(
            name='Computers',
        ),
        migrations.DeleteModel(
            name='FluorescentTube',
        ),
        migrations.DeleteModel(
            name='HistoricalData',
        ),
        migrations.DeleteModel(
            name='HistoryData',
        ),
        migrations.DeleteModel(
            name='Meter1',
        ),
        migrations.DeleteModel(
            name='Meter2',
        ),
        migrations.DeleteModel(
            name='Meter3',
        ),
        migrations.DeleteModel(
            name='MeterReading',
        ),
        migrations.DeleteModel(
            name='Printer',
        ),
    ]
