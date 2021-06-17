"""
    Check out class.
"""


class CheckOut:
    def __init__(self):
        self.prices={}
        self.total = 0

    def add_item_price(self, item: str, price: float) -> None:
        """
            A method to add price to item.
        Args:
            item (str):
            price (float):
        Returns:
            None
        """
        self.prices[item]=price

    def add_item(self, item: str) -> None:
        """
            A method to add item.
        Args:
            item (str):
        Returns:
            None
        """
        self.total+=self.prices[item]

    def compute_total(self) -> None:
        """
            Compute total for multiple items
        Returns:
            None
        """
        return self.total
