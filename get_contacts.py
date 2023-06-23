import platform

import requests

# TODO: Getting keys needs to be condition based on environment. locally
#  from .env
#  and on Github with Github Secrets

if platform.system() == 'Darwin':
    from dotenv import dotenv_values

    config = dotenv_values(".env")
    url = config['SECRET_SANTA_JSON_URL']
    key = config['SECRET_SANTA_JSON_API_KEY']
    

def get_contacts(json_url, api_key):
    headers = {
        'X-Master-Key': api_key
    }

    req = requests.get(json_url, json=None, headers=headers)
    return req.text


print(get_contacts(url, key))
