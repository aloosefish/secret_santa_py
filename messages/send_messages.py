import os
import platform

from twilio.rest import Client
from dotenv import dotenv_values

account_sid = None
auth_token = None
phone_number = None

# for running locally on a Mac, will need to update for running via Github
# Actions
if platform.system() == 'Darwin':
    config = dotenv_values(".env")
    account_sid = config['TWILIO_ACCOUNT_SID']
    auth_token = config['TWILIO_AUTH_TOKEN']
    phone_number = config['TWILIO_PHONE_NUMBER']

client = Client(account_sid, auth_token)