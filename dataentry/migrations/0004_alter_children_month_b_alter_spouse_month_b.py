# Generated by Django 4.2 on 2023-07-29 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataentry', '0003_alter_children_month_b_alter_spouse_month_b'),
    ]

    operations = [
        migrations.AlterField(
            model_name='children',
            name='month_B',
            field=models.PositiveBigIntegerField(),
        ),
        migrations.AlterField(
            model_name='spouse',
            name='month_B',
            field=models.PositiveIntegerField(),
        ),
    ]