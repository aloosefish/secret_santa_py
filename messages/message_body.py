def create_message_body(person):
    return f"Merry Christmas + {person.name}! \n\nYour Secret Santa this " \
           f"year is {person.secret_santa.name}." \
           f"\n\nHo ho ho," \
           f"\nRobot Santa"
