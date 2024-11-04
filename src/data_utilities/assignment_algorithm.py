import random

from src.data_utilities.contact_types import Contact, SecretSanta


def assign_secret_santa(list_of_contacts: list[Contact]):
    selected: list[SecretSanta] = []
    secret_santas_assigned: list[Contact] = list_of_contacts.copy()
    for i, c in enumerate(list_of_contacts):
        not_me = remove_me(c["name"], list_of_contacts)
        not_me_or_my_spouse = remove_spouse(c, not_me)
        not_selected = remove_already_selected(not_me_or_my_spouse, selected)
        choose_one = random.choice(not_selected)

        this_secret_santa: SecretSanta = {
            "name": choose_one["name"],
            "phone": choose_one["phone"],
        }

        secret_santas_assigned[i]["secret_santa"] = this_secret_santa
        selected.append(this_secret_santa)

    return secret_santas_assigned


# run `assign_secret_santa` repeatedly until all secret santas are unique.
def validate_secret_santa(contacts):
    while True:
        contacts_with_assignments = assign_secret_santa(contacts)
        # Extract Secret Santa names
        secret_santa_names = [
            contact["secret_santa"]["name"]
            for contact in contacts_with_assignments
            if "secret_santa" in contact and contact["secret_santa"] is not None
        ]
        if len(secret_santa_names) != len(contacts_with_assignments):
            continue
        else:
            return contacts_with_assignments


def remove_me(me: str, possible_combos: list[dict]):
    return [s for s in possible_combos if s["name"] != me]


# remove elements from list_a that are in list_b
def remove_already_selected(list_to_query: list[dict], selected: list[dict]):
    without_already_selected = list_to_query.copy()
    for selected_item in range(len(selected)):
        for listed_item in list_to_query:
            if selected_item == listed_item:
                without_already_selected.remove(listed_item)
    return without_already_selected


def remove_spouse(me: dict, possible_combos: list[dict]):
    return [s for s in possible_combos if s["name"] != me["spouse"]]
