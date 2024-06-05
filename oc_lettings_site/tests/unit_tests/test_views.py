import pytest
from django.test import RequestFactory
from django.urls import reverse
from oc_lettings_site.views import index


class TestOcLettingsSiteView:
    @pytest.mark.django_db
    def test_index_view(self):
        factory = RequestFactory()
        request = factory.get(reverse("index"))
        response = index(request)

        print(response)

        assert response.status_code == 200
