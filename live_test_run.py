# one-off live test: sends a single email in the same format as manual_run.py
# from ROBOT_SANTA_EMAIL to TEST_EMAIL.
import os
import smtplib
from email.message import EmailMessage

from dotenv import load_dotenv

from src.data_utilities.contact_types import Contact
from src.messages.message_bodies import create_secret_santa_message

load_dotenv()

sender_email_address = os.environ["ROBOT_SANTA_EMAIL"]
fastmail_app_password = os.environ["FASTMAIL_APP_PASSWORD"]
test_email_address = os.environ["TEST_EMAIL"]


def main():
    test_contact: Contact = {
        "name": "Test Person",
        "phone": "",
        "email": test_email_address,
        "spouse": None,
        "secret_santa": {"name": "Test Santa", "phone": ""},
    }
    secret_santa_message = create_secret_santa_message(test_contact)

    msg = EmailMessage()
    msg["From"] = sender_email_address
    msg["To"] = test_email_address
    msg["Subject"] = "Merry Christmas from Robot Santa"
    msg.set_content(secret_santa_message)

    with smtplib.SMTP_SSL("smtp.fastmail.com", 465) as client:
        client.login(sender_email_address, fastmail_app_password)
        client.send_message(msg)
    print(f"sent test email to {test_email_address}")


if __name__ == "__main__":
    main()
