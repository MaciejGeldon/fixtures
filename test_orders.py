import pytest

from orders import Order


@pytest.fixture
def order():
    return Order('socks', 10, 3)


class TestOrder:
    def test_order_total_price(self, order):
        assert order.total_cost == order.unit_price * order.quantity
