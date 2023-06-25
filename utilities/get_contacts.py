import platform

import requests

from dotenv import dotenv_values

url = None
key = None

# for running locally on a Mac, will need to update for running via Github
# Actions
if platform.system() == 'Darwin':
    config = dotenv_values(".env")
    url = config['SECRET_SANTA_JSON_URL']
    key = config['SECRET_SANTA_JSON_API_KEY']


def get_contacts(json_url, api_key):
    headers = {
        'X-Master-Key': api_key
    }

    req = requests.get(json_url, json=None, headers=headers)
    json_response = req.json()
    return json_response.get('record')


print(get_contacts(url, key))
