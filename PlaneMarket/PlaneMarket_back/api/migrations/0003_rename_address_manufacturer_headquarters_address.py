# Generated by Django 5.1.7 on 2025-04-20 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_manufacturer_remove_vacancy_company_customer_plane_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='manufacturer',
            old_name='address',
            new_name='headquarters_address',
        ),
    ]
