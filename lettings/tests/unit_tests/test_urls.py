import pytest

from django.urls import resolve, reverse
from pytest_django.asserts import assertTemplateUsed


class TestLettingUrls:
    @pytest.mark.django_db
    def test_letting_url(self, client):
        assert reverse("lettings:index") == "/lettings/"
        assert resolve("/lettings/").view_name == "lettings:index"

        response = client.get("/lettings/")
        assert response.status_code == 200
        assertTemplateUsed(response, "lettings/index.html")

    @pytest.mark.django_db
    def test_letting_detail_url(self, client, dummy_letting):
        assert (
            reverse("lettings:letting", args=[dummy_letting.id])
            == f"/lettings/{dummy_letting.id}/"
        )
        assert resolve(f"/lettings/{dummy_letting.id}/").view_name == "lettings:letting"

        response = client.get(f"/lettings/{dummy_letting.id}/")
        assert response.status_code == 200
        assertTemplateUsed(response, "lettings/letting.html")

    @pytest.mark.django_db
    def test_letting_detail_not_found(self, client):
        response = client.get("/lettings/dummy_id")
        assert response.status_code == 404
