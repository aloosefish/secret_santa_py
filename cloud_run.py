from sys import argv
from src.messages.send_emails import send_email_messages
from src.data_utilities.get_contacts import get_contacts
from src.data_utilities.assignment_algorithm import assign_secret_santa

# GitHub Action will send Environment Secrets from arguments

json_data_url = argv[1]
json_data_key = argv[2]
sendgrid_key = argv[3]
sendgrid_robot_email_sender = argv[4]


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
