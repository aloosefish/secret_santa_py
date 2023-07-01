from secret_santa_data_utilities.get_contacts import get_contacts
from secret_santa_data_utilities.make_combinations import make_combinations, inject_secret_santas
# from messages.message_body import create_message_body

import platform

import keyring

url = None
key = None

# for running locally on a Mac, will need to update for running via GitHub
# Actions
if platform.system() == 'Darwin':
    url = keyring.get_password('system', 'SECRET_SANTA_JSON_URL')
    key = keyring.get_password('system', 'SECRET_SANTA_JSON_API_KEY')


def main():
    contacts = get_contacts(url, key)
    # print(f"contacts = {contacts}")
    combos = make_combinations(contacts)
    # print(f"combos = {combos}")
    combined = inject_secret_santas(combos, contacts)
    print(f"combined = {combined}")
    print(len(contacts) == len(combos))
    # for c in combos:
    #     body = create_message_body(c.name)
    #     number = c.phone_number


if __name__ == '__main__':
    main()
