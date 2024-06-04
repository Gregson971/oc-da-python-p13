# Generated by Django 3.0 on 2024-06-04 14:09

from django.db import migrations


# Fill the new tables with data from the old table
def fill_new_tables(apps, schema_editor):
    OcLettingsSiteProfile = apps.get_model('oc_lettings_site', 'Profile')
    Profile = apps.get_model('profiles', 'Profile')

    for old_profile in OcLettingsSiteProfile.objects.all():
        Profile.objects.create(
            user=old_profile.user,
            favorite_city=old_profile.favorite_city,
        )


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(fill_new_tables),
    ]
