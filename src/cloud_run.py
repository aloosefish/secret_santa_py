from twilio.rest import Client
import argparse

from src.messages.send_messages import send_text_messages
from src.data_utilities.get_contacts import get_contacts
from src.data_utilities.assignment_algorithm import \
    assign_secret_santa

parser = argparse.ArgumentParser(prog='SecretSanta',
                                 description='create Secret Santa '
                                             'assignments and text messages '
                                             'notifications')
parser.add_argument('twilio_account_sid')
parser.add_argument('twilio_auth_token')
parser.add_argument('twilio_phone_number')
parser.add_argument('json_data_url')
parser.add_argument('json_data_key')
args = parser.parse_args()

twilio_account_sid = args.twilio_account_sid
twilio_auth_token = args.twilio_auth_token
twilio_phone_number = args.twilio_phone_number
json_data_url = args.json_data_url
json_data_key = args.json_data_key

client = Client(twilio_account_sid, twilio_auth_token)


def main():
    contacts = get_contacts(json_data_url, json_data_key)
    assigned_secret_santas = assign_secret_santa(contacts)
    send_text_messages(contacts=assigned_secret_santas,
                       robot_phone_number=twilio_phone_number,
                       twilio_client=client)


if __name__ == '__main__':
    main()
