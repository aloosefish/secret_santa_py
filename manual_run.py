# this is the same as cloud_run.py except it gets environment variables from
# local .env file instead of GitHub Secrets
from src.data_utilities.get_contacts import get_contacts

from src.data_utilities.assignment_algorithm import validate_secret_santa
from src.messages.send_emails_with_smtp import send_email_messages

import os
from dotenv import load_dotenv

load_dotenv()

json_data_url = os.environ.get("SECRET_SANTA_JSON_URL")
json_data_key = os.environ.get("SECRET_SANTA_JSON_API_KEY")
sender_email_address = os.environ.get("ROBOT_SANTA_EMAIL")
fastmail_app_password = os.environ.get("FASTMAIL_APP_PASSWORD")


def main():
    contacts = get_contacts(json_data_url, json_data_key)
    assigned_secret_santas = validate_secret_santa(contacts)
    send_email_messages(
        fastmail_app_password,
        sender_email_address,
        assigned_secret_santas,
    )


if __name__ == "__main__":
    main()
