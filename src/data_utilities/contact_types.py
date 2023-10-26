from typing import TypedDict, Optional


class SecretSanta(TypedDict):
    name: str
    phone: str


class Contact(TypedDict):
    name: str
    phone: str
    spouse: Optional[str]
    secret_santa: Optional[SecretSanta]
