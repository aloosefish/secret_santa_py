from twilio.rest import Client
import keyring

from .data_utilities.get_contacts import get_contacts
from .data_utilities.assignment_algorithm import \
    assign_secret_santa
from .messages.send_messages import send_text_messages

# For running locally. Must run `keyring.set_password` for each of
# these before running this.

twilio_account_sid = keyring.get_password('system', 'TWILIO_ACCOUNT_SID')
twilio_auth_token = keyring.get_password('system', 'TWILIO_AUTH_TOKEN')
twilio_phone_number = keyring.get_password('system',
                                           'TWILIO_PHONE_NUMBER')
json_data_url = keyring.get_password('system', 'SECRET_SANTA_JSON_URL')
json_data_key = keyring.get_password('system', 'SECRET_SANTA_JSON_API_KEY')

client = Client(twilio_account_sid, twilio_auth_token)


def main():
    contacts = get_contacts(json_data_url, json_data_key)
    assigned_secret_santas = assign_secret_santa(contacts)
    send_text_messages(contacts=assigned_secret_santas,
                       robot_phone_number=twilio_phone_number,
                       twilio_client=client)


if __name__ == '__main__':
    main()
