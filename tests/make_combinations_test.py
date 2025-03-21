import pytest

from src.data_utilities.assignment_algorithm import (
    remove_me,
    remove_spouse,
    assign_secret_santa,
)
from test_helpers.create_test_data import create_test_contact_list


class TestAssignments:
    @pytest.fixture()
    def setup_test_data(self):
        return create_test_contact_list(10)

    def test_remove_me(self, setup_test_data):
        not_me = remove_me(setup_test_data[0]["name"], setup_test_data)
        assert not_me[0]["name"] != setup_test_data[0]["name"]

    def test_remove_spouse(self, setup_test_data):
        # first contact will always have a spouse
        not_spouse = remove_spouse(setup_test_data[0], setup_test_data)
        assert not_spouse[0] != setup_test_data[0]["spouse"]

    def test_make_combinations(self, setup_test_data):
        with_ss_assigned = assign_secret_santa(setup_test_data)
        assert len(setup_test_data) == len(with_ss_assigned)
        # every combination is correct
        for i in with_ss_assigned:
            if i["secret_santa"] is None:
                pytest.fail("A contact does not have a secret santa")
