import pytest

from src.data_utilities.assignment_algorithm import assign_secret_santa
from src.data_utilities.contact_types import Contact
from test_helpers.create_test_data import create_test_contact_list


class TestIntegrations:
    @pytest.fixture()
    def setup_test_data(self):
        contacts_list = create_test_contact_list(10)
        return contacts_list

    def test_integration(self, setup_test_data):
        assigned_secret_santas = assign_secret_santa(setup_test_data)
        assert type(assigned_secret_santas) is list
        assert len(assigned_secret_santas) != 0
