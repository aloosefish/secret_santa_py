from utilities.get_contacts import get_contacts
from utilities.make_combinations import make_combinations


def main():
    contacts = get_contacts()
    combos = make_combinations(contacts)
    # send messages
    pass


if __name__ == '__main__':
    main()
