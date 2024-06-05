import pytest

from django.test import RequestFactory
from django.urls import reverse

from profiles.views import profiles_index, profile
from profiles.models import User, Profile


@pytest.fixture
def dummy_user():
    return User.objects.create_user(
        username="testuser", email="testuser@example.com", password="testpassword"
    )


@pytest.fixture
def dummy_profile(dummy_user):
    return Profile.objects.create(user=dummy_user, favorite_city="Paris")


class TestProfilesViews:
    @pytest.mark.django_db
    def test_profiles_index_view(self):
        factory = RequestFactory()
        request = factory.get(reverse("profiles:index"))
        response = profiles_index(request)

        assert response.status_code == 200

    @pytest.mark.django_db
    def test_profiles_detail_view(self, dummy_user, dummy_profile):
        factory = RequestFactory()
        request = factory.get(reverse("profiles:profile", args=[dummy_user.username]))
        response = profile(request, dummy_user.username)

        assert response.status_code == 200
