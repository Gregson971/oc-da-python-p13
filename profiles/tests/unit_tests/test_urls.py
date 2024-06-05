import pytest

from django.urls import resolve, reverse
from pytest_django.asserts import assertTemplateUsed


class TestProfileUrls:
    @pytest.mark.django_db
    def test_profile_url(self, client):
        assert reverse("profiles:index") == "/profiles/"
        assert resolve("/profiles/").view_name == "profiles:index"

        response = client.get("/profiles/")
        assert response.status_code == 200
        assertTemplateUsed(response, "profiles/index.html")

    @pytest.mark.django_db
    def test_profile_detail_url(self, client, dummy_user, dummy_profile):
        assert (
            reverse("profiles:profile", args=[dummy_user.username])
            == f"/profiles/{dummy_user.username}/"
        )
        assert resolve(f"/profiles/{dummy_user.username}/").view_name == "profiles:profile"

        response = client.get(f"/profiles/{dummy_user.username}/")
        assert response.status_code == 200
        assertTemplateUsed(response, "profiles/profile.html")

    @pytest.mark.django_db
    def test_profile_detail_not_found(self, client):
        response = client.get("/profile/dummy_id")
        assert response.status_code == 404
