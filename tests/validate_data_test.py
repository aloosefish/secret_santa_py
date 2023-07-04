import pytest

from create_test_data import make_contacts, match_spouses


class TestValidateData:
    def test_contacts_spouses_match(self):
        contact_list = make_contacts(5)
        match_contacts = match_spouses(contact_list)
        find_spouse_within = match_contacts.copy()
        for contact in match_contacts:
            spouse_to_find = contact['spouse']
            for spouse in find_spouse_within:
                if spouse['name'] != spouse_to_find:
                    continue
                elif spouse['name'] == spouse_to_find:
                    break
                else:
                    # if it gets all the way through find_spouse_within without
                    # finding spouse, then fail
                    pytest.fail('Spouses are not reciprocal')

    def test_make_contacts(self):
        contacts = make_contacts(20)
        assert len(contacts) == 10
