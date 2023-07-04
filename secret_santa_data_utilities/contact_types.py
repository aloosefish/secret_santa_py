# TODO: See if there is a way to keep this typed while making attributes
#  accessible via dot notation -- contact.name,  contact.secret_santa
from typing import TypedDict, Optional


class SecretSanta(TypedDict):
    name: str
    phone_number: str


class Contact(TypedDict):
    name: str
    phone_number: str
    spouse: Optional[str]
    secret_santa: Optional[SecretSanta]
