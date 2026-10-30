import os

from ..data_utilities.contact_types import Contact


def create_secret_santa_message(person: Contact):
    gift_budget = os.environ["GIFT_BUDGET"]
    return (
        f"Merry Christmas {person['name']}! \n\nYour Secret Santa this "
        f"year is {person['secret_santa']['name']}.  "
        f"Remember - the most you should spend on their gift is ${gift_budget} ("
        f"or "
        f"so)."
        f"\n\nHo ho ho,"
        f"\nRobot Santa"
    )


def create_test_message(person: Contact):
    return f"This is a test message for {person['name']}."
