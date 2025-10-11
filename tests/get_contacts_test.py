import pytest
from unittest.mock import patch, Mock

from src.data_utilities.get_contacts import get_contacts


class TestGetContacts:
    @pytest.fixture
    def mock_response_data(self):
        return {
            "record": [
                {
                    "name": "John Doe",
                    "phone": "555-0100",
                    "email": "john@example.com",
                    "spouse": "Jane Doe",
                    "secret_santa": None,
                },
                {
                    "name": "Jane Doe",
                    "phone": "555-0101",
                    "email": "jane@example.com",
                    "spouse": "John Doe",
                    "secret_santa": None,
                },
            ]
        }

    @patch("src.data_utilities.get_contacts.requests.get")
    def test_get_contacts_success(self, mock_get, mock_response_data):
        # Arrange
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_get.return_value = mock_response

        test_url = "https://api.jsonbin.io/v3/b/test123"
        test_api_key = "test_api_key_12345"

        # Act
        contacts = get_contacts(test_url, test_api_key)

        # Assert
        assert len(contacts) == 2
        assert contacts[0]["name"] == "John Doe"
        assert contacts[1]["name"] == "Jane Doe"
        mock_get.assert_called_once_with(
            test_url, json=None, headers={"X-Master-Key": test_api_key}
        )

    @patch("src.data_utilities.get_contacts.requests.get")
    def test_get_contacts_with_correct_headers(self, mock_get, mock_response_data):
        # Arrange
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_get.return_value = mock_response

        test_api_key = "my_secret_key"

        # Act
        get_contacts("https://example.com", test_api_key)

        # Assert
        call_args = mock_get.call_args
        assert call_args.kwargs["headers"]["X-Master-Key"] == test_api_key

    @patch("src.data_utilities.get_contacts.requests.get")
    def test_get_contacts_returns_list(self, mock_get, mock_response_data):
        # Arrange
        mock_response = Mock()
        mock_response.json.return_value = mock_response_data
        mock_get.return_value = mock_response

        # Act
        contacts = get_contacts("https://example.com", "key")

        # Assert
        assert isinstance(contacts, list)
        assert len(contacts) > 0

