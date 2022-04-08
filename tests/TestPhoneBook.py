import unittest


class TestPhoneBook(unittest.TestCase):
    def test_add_contact(self)->None:
        """
            A method to test the add contact method of phonebook.
        Returns:
            None
        """
        phonebook=PhoneBook()
        phonebook.add_contact('Tarbo','647-678-1352')
        number=phonebook.get_contact_by_name('Tarbo')
        self.assertEqual('647-678-1352',number)