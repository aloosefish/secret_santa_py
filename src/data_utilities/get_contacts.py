import requests
from src.data_utilities.contact_types import Contact


def get_contacts(json_url, api_key):
    headers = {"X-Master-Key": api_key}

    try:
        req = requests.get(json_url, json=None, headers=headers)
        req.raise_for_status()  # Raises HTTPError for bad status codes
    except requests.exceptions.RequestException as e:
        raise ValueError(f"Failed to fetch contacts: {e}")

    json_response = req.json()
    records = json_response.get("record")

    if records is None:
        raise ValueError(
            f"No 'record' field in API response. Keys: {list(json_response.keys())}"
        )

    contacts: list[Contact] = list(records)
    return contacts
