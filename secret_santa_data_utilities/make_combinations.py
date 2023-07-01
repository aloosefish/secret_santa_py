import random

from contact_types import Contact


# TODO: Fix this. Currently, this code makes everyone their own
#  secret santa. With the correct data structure, but not the correct values
def make_combinations(list_of_contacts: list[Contact]):
    combos = []
    selected = []
    for c in list_of_contacts:
        not_me = remove_me(c['name'], list_of_contacts)
        not_me_or_my_spouse = remove_spouse(c, not_me)
        not_selected = remove_already_selected(not_me_or_my_spouse, selected)
        secret_santa = random.choice(not_selected)

        secret_santa_name = secret_santa['name']
        secret_santa_phone = secret_santa['phone_number']
        add_to_combo = {"name": secret_santa_name,
                        "phone": secret_santa_phone}
        combos.append(add_to_combo)
        selected.append(secret_santa)

    return combos


def remove_me(me: str, possible_combos: list[dict]):
    return [s for s in possible_combos if s['name'] != me]


# remove elements from list_a that are in list_b
def remove_already_selected(list_to_query: list[dict], selected: list[dict]):
    without_already_selected = list_to_query.copy()
    for selected_item in range(len(selected)):
        for listed_item in list_to_query:
            if selected_item == listed_item:
                without_already_selected.remove(listed_item)
    return without_already_selected


def remove_spouse(me: dict, possible_combos: list[dict]):
    return [s for s in possible_combos if s['name'] != me['spouse']]


# each contact is their own secret santa
def inject_secret_santas(secret_santas, contacts) -> list[Contact]:
    secret_santas_assigned = contacts.copy()
    for i, contents in enumerate(secret_santas_assigned):
        secret_santas_assigned[i]['secret_santa'] = secret_santas[i]

    return secret_santas_assigned
