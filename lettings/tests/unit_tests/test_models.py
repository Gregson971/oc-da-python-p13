import pytest


class TestLettingModels:
    @pytest.mark.django_db
    def test_letting_str(self, dummy_letting):
        assert str(dummy_letting) == "Bel appartement"

    @pytest.mark.django_db
    def test_address_str(self, dummy_address):
        assert str(dummy_address) == "1 rue de la paix"
