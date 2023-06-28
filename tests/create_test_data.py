import math
import random

from faker import Faker

from contact_types import Contact

fake = Faker(locale='en_US')


def create_test_contacts(n: int):
    fake_contacts = []

    for i in range(n):
        name = fake.first_name()
        phone_number = fake.phone_number()
        contact = {'name': name, 'phone_number': phone_number}
        fake_contacts.append(contact)

    return fake_contacts


# TODO: Fix this: Currently not quite right. Spouse assignment is being
#  made, kind of. Spouses need to be reciprocal. Also, resulting output is
#  list[
#  list[dict]] -- one too many
#  dimension
#  of list. And spouse is
# add spouses to some of the contacts
def add_spouses(list_of_test_contacts):
    no_spouse: int
    if len(list_of_test_contacts) % 2 == 0:
        no_spouse = 2
    else:
        no_spouse = 3

    contacts_with_spouses = random.sample(list_of_test_contacts,
                                          len(list_of_test_contacts)
                                          - no_spouse)

    contacts_without_spouses = [x for x in list_of_test_contacts +
                                contacts_with_spouses if
                                x not in contacts_with_spouses]

    for index, contact in enumerate(contacts_with_spouses):
        # spouse from random choice of not index.
        without_index = contacts_with_spouses[index:]
        spouse = random.choice(without_index)
        contacts_with_spouses[index]['spouse'] = spouse

    return [contacts_with_spouses, contacts_without_spouses]


test_contacts = create_test_contacts(10)
some_with_spouses = add_spouses(test_contacts)
print(some_with_spouses)
