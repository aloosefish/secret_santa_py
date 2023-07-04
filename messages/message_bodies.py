from secret_santa_data_utilities.contact_types import Contact


def create_secret_santa_message(person: Contact):
    return f"Merry Christmas + {person['name']}! \n\nYour Secret Santa this " \
           f"year is {person['secret_santa']['name']}." \
           f"\n\nHo ho ho," \
           f"\nRobot Santa"


def create_test_message(person: Contact):
    return f"This is a test message for {person['name']}."
