"""Discount calculator used for Lab 6 coverage analysis."""


def calculate_discount(price: float, is_member: bool) -> float:
    """Return the final price after applicable member and price discounts."""
    discount = 0.0
    if is_member:
        discount = 0.10
    if price > 100:
        discount += 0.05
    return price * (1 - discount)
