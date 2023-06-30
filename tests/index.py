from utilities.make_combinations import inject_secret_santas, make_combinations
from tests.create_test_data import create_test_contact_list


def app_flow():
    contacts = create_test_contact_list(5)
    combos = make_combinations(contacts)
    combined = inject_secret_santas(combos, contacts)
    print(combined)


app_flow()
