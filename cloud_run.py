# TODO: This will pull values from GitHub secrets. Need to figure out how to
#  pass these values to this script -- probably just command line arguments
from twilio.rest import Client

from secret_santa_data_utilities.get_contacts import get_contacts
from secret_santa_data_utilities.secret_santa_assignment_algorithm import \
    assign_secret_santa

twilio_account_sid = 'None'
twilio_auth_token = 'None'
twilio_phone_number = None
json_data_url = None
json_data_key = None

client = Client(twilio_account_sid, twilio_auth_token)


def main():
    contacts = get_contacts(json_data_url, json_data_key)
    combos = assign_secret_santa(contacts)
    # send messages


if __name__ == '__main__':
    main()
