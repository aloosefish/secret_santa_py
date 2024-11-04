import pytest
from src.data_utilities.assignment_algorithm import validate_secret_santa


# Mock function to simulate the behavior of assign_secret_santa
def mock_assign_secret_santa(contacts):
    # This mock function will just return the contacts with a simple assignment
    for i, contact in enumerate(contacts):
        contact["secret_santa"] = {"name": contacts[(i + 1) % len(contacts)]["name"]}
    return contacts


# Patch the assign_secret_santa function in the module
@pytest.fixture(autouse=True)
def patch_assign_secret_santa(monkeypatch):
    monkeypatch.setattr(
        "src.data_utilities.assignment_algorithm.assign_secret_santa",
        mock_assign_secret_santa,
    )


@pytest.mark.parametrize(
    "contacts, expected",
    [
        # Happy path with three contacts
        pytest.param(
            [{"name": "Alice"}, {"name": "Bob"}, {"name": "Charlie"}],
            [
                {"name": "Alice", "secret_santa": {"name": "Bob"}},
                {"name": "Bob", "secret_santa": {"name": "Charlie"}},
                {"name": "Charlie", "secret_santa": {"name": "Alice"}},
            ],
            id="happy_path_three_contacts",
        ),
        # Happy path with two contacts
        pytest.param(
            [{"name": "Alice"}, {"name": "Bob"}],
            [
                {"name": "Alice", "secret_santa": {"name": "Bob"}},
                {"name": "Bob", "secret_santa": {"name": "Alice"}},
            ],
            id="happy_path_two_contacts",
        ),
        # Edge case with one contact
        pytest.param(
            [{"name": "Alice"}],
            [{"name": "Alice", "secret_santa": {"name": "Alice"}}],
            id="edge_case_one_contact",
        ),
        # Edge case with no contacts
        pytest.param([], [], id="edge_case_no_contacts"),
    ],
)
def test_validate_secret_santa(contacts, expected):
    # Act
    result = validate_secret_santa(contacts)

    # Assert
    assert result == expected


@pytest.mark.parametrize(
    "contacts, expected_exception",
    [
        # Error case with missing 'name' key
        pytest.param(
            [{"name": "Alice"}, {"name": "Bob"}, {}],
            KeyError,
            id="error_case_missing_name_key",
        ),
        # Error case with non-dict contact
        pytest.param(
            [{"name": "Alice"}, "Bob", {"name": "Charlie"}],
            TypeError,
            id="error_case_non_dict_contact",
        ),
    ],
)
def test_validate_secret_santa_errors(contacts, expected_exception):
    # Act and Assert
    with pytest.raises(expected_exception):
        validate_secret_santa(contacts)
