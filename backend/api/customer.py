"""Example backend API boundary for the UI gallery."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Customer:
    """Backend-owned customer data returned as JSON by a real API later."""

    name: str
    balance: str


def get_customer(customer_id: int) -> Customer:
    """Return example data without exposing backend objects to the frontend."""
    if customer_id < 1:
        raise ValueError("customer_id must be positive")
    return Customer(name="Pragion User", balance="Rs. 25,000")
