# Generated by Django 3.0 on 2024-06-04 13:35

from django.db import migrations


# Fill the new tables with data from the old table
def fill_new_tables(apps, schema_editor):
    try:
        OcLettingsSiteLetting = apps.get_model('oc_lettings_site', 'Letting')
    except LookupError:
        return

    Address = apps.get_model('lettings', 'Address')
    Letting = apps.get_model('lettings', 'Letting')

    for old_letting in OcLettingsSiteLetting.objects.all():
        address = Address.objects.create(
            number=old_letting.address.number,
            street=old_letting.address.street,
            city=old_letting.address.city,
            state=old_letting.address.state,
            zip_code=old_letting.address.zip_code,
            country_iso_code=old_letting.address.country_iso_code,
        )
        Letting.objects.create(title=old_letting.title, address=address)


class Migration(migrations.Migration):

    dependencies = [
        ('lettings', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(fill_new_tables),
    ]
