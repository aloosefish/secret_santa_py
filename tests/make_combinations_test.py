import pytest

from secret_santa_data_utilities.make_combinations import remove_me, \
    remove_spouse
from create_test_data import create_test_contact_list


class TestCombinations:
    @pytest.fixture()
    def setup_test_data(self):
        contacts_list = create_test_contact_list(10)
        return contacts_list

    def test_remove_me(self, setup_test_data):
        # first contact will always have a spouse
        not_me = remove_me(setup_test_data[0]['name'], setup_test_data)
        assert not_me[0]['name'] != setup_test_data[0]['name']

    def test_remove_spouse(self, setup_test_data):
        not_spouse = remove_spouse(setup_test_data[0],
                                   setup_test_data)
        assert not_spouse[0] != setup_test_data[0]['spouse']
