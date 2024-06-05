import pytest

from django.test import Client
from profiles.models import User, Profile


@pytest.fixture
def client():
    return Client()


@pytest.fixture
def dummy_user():
    return User.objects.create_user(
        username="testuser", email="testuser@example.com", password="testpassword"
    )


@pytest.fixture
def dummy_profile(dummy_user):
    return Profile.objects.create(user=dummy_user, favorite_city="Paris")
