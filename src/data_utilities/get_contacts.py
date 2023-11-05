import requests

from src.data_utilities.contact_types import Contact


def get_contacts(json_url, api_key):
    headers = {"X-Master-Key": api_key}

    req = requests.get(json_url, json=None, headers=headers)
    json_response = req.json()
    records = json_response.get("record")
    contacts: list[Contact] = []
    #  TypeError: 'NoneType' object is not iterable
    for i in records:
        contacts.append(i)
    return contacts
