"""
    A test module for the checkout class.
"""
from src.CheckOut import CheckOut
from pytest import fixture


@fixture()
def checkout() -> object:
    checkout = CheckOut()
    return checkout


def test_compute_total(checkout) -> None:
    """
        Test the computation of total items for multiple items.
    Args:
        checkout (object):
    Returns:
        None
    """
    checkout.add_item_price("item1", 4)
    checkout.add_item("item1")
    checkout.add_item_price("item2", 6)
    checkout.add_item("item2")
    assert checkout.compute_total() == 10
