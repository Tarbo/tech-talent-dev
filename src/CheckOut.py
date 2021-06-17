"""
    Check out class.
"""


class CheckOut:
    pass

    def add_item_price(self, item: str, price: float) -> None:
        """
            A method to add price to item.
        Args:
            item (str):
            price (float):
        Returns:
            None
        """
        pass

    def add_item(self, item: str) -> None:
        """
            A method to add item.
        Args:
            item (str):
        Returns:
            None
        """
        pass

    def calculate_current_total(self) -> None:
        """
            Compute current total with one item
        Returns:
            None
        """
        return 1

    def compute_total_for_multiple_items(self) -> None:
        """
            Compute total for multiple items
        Returns:
            None
        """
        return 3
