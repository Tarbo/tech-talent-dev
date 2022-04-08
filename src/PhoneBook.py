"""
    A module for the phonebook class.
"""


class PhoneBook:
    def __init__(self):
        self.contact = dict()

    def add_contact(self, name: str, number: str) -> None:
        """
            A module to add the contact name and number.
        Args:
            name (str): Contact name.
            number (str): Contact number.

        Returns:
            None.
        """
        self.contact[name] = number
