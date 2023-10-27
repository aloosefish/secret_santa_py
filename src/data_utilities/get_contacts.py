import requests

from src.data_utilities.contact_types import Contact


def get_contacts(json_url, api_key) -> list[Contact]:
    headers = {"X-Master-Key": api_key}

    req = requests.get(json_url, json=None, headers=headers)
    json_response = req.json()
    # this is a list of dicts need to make this a list[Contact] for it to
    # work with assign_secret_santa function
    records = json_response.get("record")
    contacts: list[Contact] = []
    for i in records():
        contacts.append(i)
    return contacts
