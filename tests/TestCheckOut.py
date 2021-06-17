"""
    A test module for the checkout class.
"""
from src.CheckOut import CheckOut
from pytest import fixture


@fixture()
def checkout() -> object:
    checkout = CheckOut()
    return checkout


def test_calculate_current_total(checkout) -> None:
    """
        Test whether we can calculate current total.
    Args:
        checkout (object):
    Returns:
        None
    """
    checkout.add_item_price("item", 56)
    checkout.add_item("item")
    assert checkout.calculate_current_total() == 1