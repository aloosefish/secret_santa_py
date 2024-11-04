from src.data_utilities.contact_types import Contact
from faker import Faker

fake = Faker(locale="en_US")


def make_contacts(n: int):
    contacts: list[Contact] = []
    for i in range(n // 2):
        contact: Contact = {
            "name": fake.name(),
            "phone": fake.phone_number(),
            "email": f"{fake.name}@anything.fake",
            "spouse": fake.name(),
            "secret_santa": None,
        }

        contacts.append(contact)
    return contacts


def match_spouses(unmatched: list):
    fake_contacts_matching_spouse: list[Contact] = []
    for j in unmatched:
        contact: Contact = {
            "name": j["spouse"],
            "phone": fake.phone_number(),
            "email": f"{fake.name}@anything.fake",
            "spouse": j["name"],
            "secret_santa": None,
        }

        fake_contacts_matching_spouse.append(contact)
    return fake_contacts_matching_spouse + unmatched


def make_singles(n: int):
    singles: list[Contact] = []
    for single in range(n):
        this_contact: Contact = {
            "name": fake.name(),
            "phone": fake.phone_number(),
            "email": f"{fake.name}@anything.fake",
            "spouse": None,
            "secret_santa": None,
        }

        singles.append(this_contact)

    return singles


def create_test_contact_list(size: int):
    contacts = make_contacts(size)
    contacts_with_spouses = match_spouses(contacts)
    singles = make_singles(3)

    return contacts_with_spouses + singles
