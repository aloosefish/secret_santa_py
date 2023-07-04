# extract all but send_messages and twilio client to separate file with
# platform setup details a function that takes params for local and GitHub
# Actions environments
# import os
import platform

from twilio.rest import Client
import keyring

account_sid = None
auth_token = None
twilio_phone_number = None

# for running locally on a Mac. Will need to update for running via GitHub
# Actions
if platform.system() == 'Darwin':
    account_sid = keyring.get_password('system', 'TWILIO_ACCOUNT_SID')
    auth_token = keyring.get_password('system', 'TWILIO_AUTH_TOKEN')
    twilio_phone_number = keyring.get_password('system', 'TWILIO_PHONE_NUMBER')

client = Client(account_sid, auth_token)


def send_message(message_contents, recipient_number):
    message = client.messages.create(body=message_contents,
                                     from_=twilio_phone_number,
                                     to=recipient_number)
