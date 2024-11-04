import yagmail

from ..data_utilities.contact_types import Contact
from ..messages.message_bodies import create_secret_santa_message


def send_email_messages(
    api_key: str,
    robot_email_sender: str,
    contacts: list[Contact],
):
    yag = yagmail.SMTP(robot_email_sender, api_key)
    for i in contacts:
        secret_santa_message = create_secret_santa_message(i)

        try:
            yag.send(
                to_emails=i["email"],
                subject="Merry Christmas from Robot Santa",
                contents=secret_santa_message,
            )
        except Exception as e:
            print(e)
