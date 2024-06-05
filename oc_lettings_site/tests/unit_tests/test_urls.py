import pytest

from django.test import Client
from django.urls import resolve, reverse
from pytest_django.asserts import assertTemplateUsed


@pytest.fixture
def client():
    return Client()


class TestHomeUrls:
    @pytest.mark.django_db
    def test_home_url(self, client):
        assert reverse("index") == "/"
        assert resolve("/").view_name == "index"

        response = client.get("/")
        assert response.status_code == 200
        assertTemplateUsed(response, "index.html")

    @pytest.mark.django_db
    def test_admin_url(self):
        assert reverse("admin:index") == "/admin/"
        assert resolve("/admin/").view_name == "admin:index"

    @pytest.mark.django_db
    def test_home_url_not_found(self, client):
        response = client.get("/letting")
        assert response.status_code == 404
