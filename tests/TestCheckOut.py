"""
    A test module for the checkout class.
"""
from src.CheckOut import CheckOut
from pytest import fixture


@fixture()
def checkout() -> object:
    checkout = CheckOut()
    return checkout

def test_compute_total_for_multiple_items(checkout)->None:
    """
        Test the computation of total items for multiple items.
    Args:
        checkout (object):
    Returns:
        None
    """
    checkout.add_item_price("item1", 56)
    checkout.add_item("item1")
    checkout.add_item_price("item2", 96)
    checkout.add_item("item2")
    assert checkout.compute_total_for_multiple_items() == 3
