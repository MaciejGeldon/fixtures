import pytest

from orders import Item, Bucket


@pytest.fixture
def item():
    return Item('socks', 10, 3)


@pytest.fixture
def bucket(item):
    return Bucket('cloths', [item])


class TestOrder:
    def test_order_total_price(self, item):
        assert item.total_cost == item.unit_price * item.quantity

    def test_bucket_with_single_item(self, bucket, item):
        assert item.total_cost == bucket.total_cost
