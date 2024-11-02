# this is the same as cloud_run.py except it gets environment variables from
# local .env file instead of GitHub Secrets

import os
from dotenv import load_dotenv

load_dotenv()

from src.data_utilities.get_contacts import get_contacts
from src.data_utilities.assignment_algorithm import assign_secret_santa
from src.messages.send_emails import send_email_messages

json_data_url = os.environ.get("SECRET_SANTA_JSON_URL")
json_data_key = os.environ.get("SECRET_SANTA_JSON_API_KEY")
sendgrid_key = os.environ.get("SecretSantaAPIKey")
sendgrid_robot_email_sender = os.environ.get("SENDGRID_ROBOT_EMAIL")


def main():
    contacts = get_contacts(json_data_url, json_data_key)
    assigned_secret_santas = assign_secret_santa(contacts)
    send_email_messages(
        sendgrid_key,
        sendgrid_robot_email_sender,
        assigned_secret_santas,
    )


if __name__ == "__main__":
    main()
