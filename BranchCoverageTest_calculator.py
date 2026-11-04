"""Branch-coverage-focused tests required by Lab 6."""

import pytest

from calculator import calculate_discount


@pytest.mark.parametrize(
    ("price", "is_member", "expected"),
    [
        (150, True, 127.5),   # member and expensive item
        (100, True, 90.0),    # member and price boundary
        (150, False, 142.5),  # non-member and expensive item
        (100, False, 100.0),  # non-member and price boundary
    ],
)
def test_all_discount_decision_branches(
    price: float, is_member: bool, expected: float
) -> None:
    """Exercise both outcomes of both discount decisions."""
    assert calculate_discount(price, is_member) == expected
