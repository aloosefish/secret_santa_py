import platform

import keyring
import requests

url = None
key = None

# for running locally on a Mac, will need to update for running via Github
# Actions
if platform.system() == 'Darwin':
    url = keyring.get_password('system', 'SECRET_SANTA_JSON_URL')
    key = keyring.get_password('system', 'SECRET_SANTA_JSON_API_KEY')


def get_contacts(json_url, api_key):
    headers = {
        'X-Master-Key': api_key
    }

    req = requests.get(json_url, json=None, headers=headers)
    json_response = req.json()
    return json_response.get('record')


print(get_contacts(url, key))
