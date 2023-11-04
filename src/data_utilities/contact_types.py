from typing import TypedDict, Optional


class SecretSanta(TypedDict):
    name: str
    phone: str


class Contact(TypedDict):
    name: str
    phone: str
    email: str
    spouse: Optional[str]
    secret_santa: Optional[SecretSanta]
