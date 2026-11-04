"""Line-coverage-focused test required by Lab 6."""

from calculator import calculate_discount


def test_member_expensive_item() -> None:
    """Executes every executable source line in calculator.py."""
    assert calculate_discount(150, True) == 127.5
