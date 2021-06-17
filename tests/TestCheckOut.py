"""
    A test module for the checkout class.
"""
from src.CheckOut import CheckOut
from pytest import fixture


@fixture()
def checkout() -> object:
    checkout = CheckOut()
    return checkout


def test_can_add_item_price(checkout) -> None:
    """
        Test case for can add item price.
    Returns:
        None
    """
    checkout.add_item_price("item", 56)


def test_add_item(checkout) -> None:
    """
        Test add item method.
    Returns:
        None
    """
    checkout.add_item("item")


def test_calculate_current_total(checkout) -> None:
    """
        Test whether we can calculate current total.
    Args:
        checkout (object):
    Returns:
        None
    """
    checkout.calculate_current_total(35, 23)