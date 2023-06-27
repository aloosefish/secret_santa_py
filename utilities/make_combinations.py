import random


def make_combinations(list_of_contacts):
    combos = []
    selected = []
    for c in list_of_contacts:
        not_me = remove_me(c['name'], list_of_contacts)
        not_spouse = remove_spouse(c['name'], not_me)
        not_selected = remove_already_selected(c['name'], selected)
        secret_santa = random.choice(not_me + not_spouse + not_selected)

        secret_santa_name = secret_santa['name']
        secret_santa_phone = secret_santa['phone']
        add_to_combo = {"name": secret_santa_name,
                        "phone": secret_santa_phone}
        combos.append(add_to_combo)
        selected.append(secret_santa)

    return combos


def remove_me(me, possible_combos):
    return [s for s in possible_combos if s['name'] == me]


def remove_already_selected(me, already_selected):
    return [s for s in already_selected if s['name'] == me]


def remove_spouse(me, possible_combos):
    for i in possible_combos:
        if i['name'] == me:
            return [s for s in possible_combos if s['spouse'] != me]
        else:
            return possible_combos


def inject_secret_santas(secret_santas, contacts):
    contacts_copied = contacts.copy()
    for i, contents in enumerate(contacts_copied):
        contacts_copied[i]['secret_santa'] = secret_santas[i]

    return contacts_copied
