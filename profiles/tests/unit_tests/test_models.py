import pytest


class TestProfileModels:
    @pytest.mark.django_db
    def test_profile_str(self, dummy_profile):
        assert str(dummy_profile) == "testuser"
