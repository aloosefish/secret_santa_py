
from test_helpers.create_test_data import make_contacts, match_spouses


class TestValidateData:
    def test_contacts_spouses_match(self):
        contact_list = make_contacts(5)
        match_contacts = match_spouses(contact_list)
        find_spouse_within = match_contacts.copy()
        for contact in match_contacts:
            spouse_to_find = contact["spouse"]
            for spouse in find_spouse_within:
                if spouse["name"] != spouse_to_find:
                    continue
                else:
                    break

    def test_make_contacts(self):
        contacts = make_contacts(20)
        assert len(contacts) == 10
