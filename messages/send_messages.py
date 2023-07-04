from twilio.rest import Client
from secret_santa_data_utilities.contact_types import Contact
from messages.message_bodies import create_secret_santa_message


def test_send_message(message_contents, recipient_number, robot_phone_number,
                      client: Client):
    client.messages.create(body=message_contents,
                           from_=robot_phone_number,
                           to=recipient_number)


def send_text_messages(contacts: list[Contact],
                       robot_phone_number,
                       twilio_client: Client):
    for i in contacts:
        message = create_secret_santa_message(i)
        twilio_client.messages.create(body=message,
                                      from_=robot_phone_number,
                                      to=i['phone_number'])
