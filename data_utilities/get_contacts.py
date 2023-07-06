import requests

from data_utilities.contact_types import Contact


def get_contacts(json_url, api_key) -> list[Contact]:
    headers = {
        'X-Master-Key': api_key
    }

    req = requests.get(json_url, json=None, headers=headers)
    json_response = req.json()
    # this is a list of dicts
    return json_response.get('record')
