import pytest

from django.test import RequestFactory
from django.urls import reverse

from lettings.views import lettings_index, letting


class TestLettingsViews:
    @pytest.mark.django_db
    def test_lettings_index_view(self):
        factory = RequestFactory()
        request = factory.get(reverse("lettings:index"))
        response = lettings_index(request)

        assert response.status_code == 200

    @pytest.mark.django_db
    def test_lettings_detail_view(self, dummy_letting):
        factory = RequestFactory()
        request = factory.get(reverse("lettings:letting", args=[dummy_letting.id]))
        response = letting(request, dummy_letting.id)

        assert response.status_code == 200
