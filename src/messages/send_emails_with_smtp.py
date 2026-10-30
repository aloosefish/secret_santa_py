import smtplib
from email.message import EmailMessage

from ..data_utilities.contact_types import Contact
from ..messages.message_bodies import create_secret_santa_message


def send_email_messages(
    api_key: str,
    robot_email_sender: str,
    contacts: list[Contact],
):
    with smtplib.SMTP_SSL("smtp.fastmail.com", 465) as client:
        client.login(robot_email_sender, api_key)
        for i in contacts:
            secret_santa_message = create_secret_santa_message(i)

            msg = EmailMessage()
            msg["From"] = robot_email_sender
            msg["To"] = i["email"]
            msg["Subject"] = "Merry Christmas from Robot Santa"
            msg.set_content(secret_santa_message)

            try:
                client.send_message(msg)
            except Exception as e:
                print(e)
