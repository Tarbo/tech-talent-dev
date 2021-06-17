"""
    A test module for the checkout class.
"""
from src.CheckOut import CheckOut
from pytest import fixture


@fixture()
def checkout() -> object:
    checkout = CheckOut()
    return checkout
