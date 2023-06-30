import random

from faker import Faker

fake = Faker(locale='en_US')


def make_contacts(n: int):
    contacts = []
    for i in range(n // 2):
        name = fake.name()
        phone_number = fake.phone_number()
        spouse = fake.name()
        contact = {'name': name, 'phone_number': phone_number, 'spouse':
            spouse}

        contacts.append(contact)
    return contacts


def match_spouses(unmatched: list):
    fake_contacts_matching_spouse = []
    for j in unmatched:
        spouse_name = j['spouse']
        spouse_phone_number = fake.phone_number()
        spouses_spouse = j['name']

        fake_contacts_matching_spouse.append(
            {'name': spouse_name, 'phone_number':
                spouse_phone_number, 'spouse': spouses_spouse})
    return fake_contacts_matching_spouse + unmatched


def make_singles(n: int):
    singles = []
    for single in range(n):
        single_name = fake.name()
        single_phone = fake.phone_number()

        singles.append({'name': single_name, 'phone_number': single_phone,
                        'spouse': None})

    return singles


def create_test_contact_list(size: int):
    contacts = make_contacts(size)
    contacts_with_spouses = match_spouses(contacts)
    singles = make_singles(3)

    return contacts_with_spouses + singles
