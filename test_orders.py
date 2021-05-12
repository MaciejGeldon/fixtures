import pytest

from orders import Item, Bucket


@pytest.fixture
def item():
    return Item('socks', 10, 3)


@pytest.fixture
def bucket(item):
    return Bucket('cloths', [item])


@pytest.fixture()
def strange_bucket(bucket):
    items = bucket.items
    items.extend([Item('cheese', 5, 1), Item('cola', 3, 5)])
    return bucket


class TestOrder:
    def test_order_total_price(self, item):
        assert item.total_cost == item.unit_price * item.quantity

    def test_bucket_with_single_item(self, bucket, item):
        assert item.total_cost == bucket.total_cost

    def test_bucket_with_more_than_one_item(self, strange_bucket):
        assert strange_bucket.total_cost == sum(
            item.total_cost for item in strange_bucket.items
        )

    def test_bucket_receipt_raise_errors_on_empty_receipt(self):
        bucket = Bucket('empty_bucket', [])
        with pytest.raises(Exception):
            bucket.receipt
