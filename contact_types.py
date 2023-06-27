from typing import TypedDict, Optional


class SecretSanta(TypedDict):
    name: str
    phone_number: str


class Contact(TypedDict):
    name: str
    phone_number: str
    spouse: Optional[str]
    secret_santa: Optional[SecretSanta]
