import pytest
from django.test import Client


from lettings.models import Letting, Address


@pytest.fixture
def client():
    return Client()


@pytest.fixture
def dummy_address():
    return Address.objects.create(
        number=1,
        street="rue de la paix",
        city="Paris",
        state="Ile de France",
        zip_code="75001",
        country_iso_code="FRA",
    )


@pytest.fixture
def dummy_letting(dummy_address):
    return Letting.objects.create(title="Bel appartement", address=dummy_address)
