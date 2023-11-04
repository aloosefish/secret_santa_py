from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from ..data_utilities.contact_types import Contact
from ..messages.message_bodies import create_secret_santa_message


def send_email_messages(
    sendgrid_api_key: str,
    sendgrid_robot_email_sender: str,
    contacts: list[Contact],
):
    for i in contacts:
        secret_santa_message = create_secret_santa_message(i)

        email_contents = Mail(
            from_email=sendgrid_robot_email_sender,
            to_emails=i["email"],
            subject='Merry Christmas from Robot Santa',
            plain_text_content=secret_santa_message,
        )
        try:
            sg = SendGridAPIClient(sendgrid_api_key)
            response = sg.send(email_contents)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(e)
