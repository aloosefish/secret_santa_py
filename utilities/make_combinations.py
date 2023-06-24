import random


def make_combinations(list_of_contacts):
    # not self
    combos = []
    selected = []
    for c in combos:
        not_me = remove_me(c.name, list_of_contacts)
        not_spouse = remove_spouse(c.name, not_me)
        not_selected = remove_already_selected(c.name, selected)
        secret_santa = random.choice(not_me + not_spouse + not_selected)
        c["secret_santa"] = {"name": secret_santa.name,
                             "phone": secret_santa.phone}
        selected.append(secret_santa)

    return combos


def remove_me(me, possible_combos):
    return [s for s in possible_combos if s.name == me]


def remove_already_selected(me, already_selected):
    return [s for s in already_selected if s.name == me]


def remove_spouse(me, possible_combos):
    if -me.spouse:
        return
    return [s for s in possible_combos if s.spouse == me.spouse]
