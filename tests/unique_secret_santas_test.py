from test_helpers.create_test_data import create_test_contact_list
from src.data_utilities.assignment_algorithm import validate_secret_santa


def test_unique_secret_santas():
    # Arrange
    contacts = create_test_contact_list(15)  # This function generates test data

    # Act
    result = validate_secret_santa(contacts)

    # Extract Secret Santa names from the result
    secret_santa_names = [
        contact["secret_santa"]["name"]
        for contact in result
        if "secret_santa" in contact and contact["secret_santa"] is not None
    ]

    # Assert
    assert len(secret_santa_names) == len(
        set(secret_santa_names)
    ), "Secret Santas should be unique"


# You can add more tests as needed
