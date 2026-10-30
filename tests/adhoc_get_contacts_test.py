"""
Ad-hoc test for troubleshooting get_contacts with real API calls.
This test is meant to be run manually and requires actual API credentials.

To run:
    uv run pytest tests/adhoc_get_contacts_test.py -v -s

Requirements:
    - Set SECRET_SANTA_JSON_URL environment variable
    - Set SECRET_SANTA_JSON_API_KEY environment variable
    
Or use a .env file in the project root.
"""

import os
import pytest
from dotenv import load_dotenv

from src.data_utilities.get_contacts import get_contacts


# Load environment variables from .env file if present
load_dotenv()


@pytest.mark.skipif(
    not os.getenv("SECRET_SANTA_JSON_URL") or not os.getenv("SECRET_SANTA_JSON_API_KEY"),
    reason="Requires SECRET_SANTA_JSON_URL and SECRET_SANTA_JSON_API_KEY environment variables"
)
class TestGetContactsRealAPI:
    def test_get_contacts_real_api(self):
        """Test get_contacts with real API call"""
        # Arrange
        json_url = os.getenv("SECRET_SANTA_JSON_URL")
        api_key = os.getenv("SECRET_SANTA_JSON_API_KEY")
        
        print("\nAttempting to fetch contacts from: {json_url[:30]}...")
        
        # Act
        contacts = get_contacts(json_url, api_key)
        
        # Assert
        print(f"\n✓ Successfully retrieved {len(contacts)} contacts")
        
        assert contacts is not None, "Contacts should not be None"
        assert isinstance(contacts, list), "Contacts should be a list"
        assert len(contacts) > 0, "Should have at least one contact"
        
        # Verify structure of first contact
        first_contact = contacts[0]
        print("\nFirst contact structure:")
        print(f"  - name: {first_contact.get('name', 'MISSING')}")
        print(f"  - email: {first_contact.get('email', 'MISSING')}")
        print(f"  - phone: {first_contact.get('phone', 'MISSING')}")
        print(f"  - spouse: {first_contact.get('spouse', 'MISSING')}")
        
        assert "name" in first_contact, "Contact should have 'name' field"
        assert "email" in first_contact, "Contact should have 'email' field"
        assert "phone" in first_contact, "Contact should have 'phone' field"
        
        print(f"\n✓ All {len(contacts)} contacts have required fields")
        
    def test_get_contacts_prints_all_data(self):
        """Debugging test that prints all contact data"""
        # Arrange
        json_url = os.getenv("SECRET_SANTA_JSON_URL")
        api_key = os.getenv("SECRET_SANTA_JSON_API_KEY")
        
        # Act
        contacts = get_contacts(json_url, api_key)
        
        # Print all contacts for inspection
        print(f"\n{'='*60}")
        print(f"RETRIEVED {len(contacts)} CONTACTS:")
        print(f"{'='*60}")
        
        for i, contact in enumerate(contacts, 1):
            print(f"\nContact {i}:")
            print(f"  Name:   {contact.get('name')}")
            print(f"  Email:  {contact.get('email')}")
            print(f"  Phone:  {contact.get('phone')}")
            print(f"  Spouse: {contact.get('spouse', 'None')}")
        
        print(f"\n{'='*60}")
        
        # Assert
        assert len(contacts) > 0

