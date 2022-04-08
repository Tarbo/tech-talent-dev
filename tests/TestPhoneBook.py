import unittest

from src.PhoneBook import PhoneBook


class TestPhoneBook(unittest.TestCase):
    def test_add_contact(self) -> None:
        """
            A method to test the add contact method of phonebook.
        Returns:
            None
        """
        phonebook = PhoneBook()
        phonebook.add_contact('Tarbo', '647-678-1352')
        number = phonebook.contact.get('Tarbo')
        self.assertEqual('647-678-1352', number)

    def test_get_contact(self) -> None:
        """
            Check whether a key error is raised for invalid name
        Returns:
            None
        """
        phonebook = PhoneBook()
        phonebook.contact['Nneka'] = '5678'
        number = phonebook.get_contact('Nneka')
        self.assertEqual('5678', number)
