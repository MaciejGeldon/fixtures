from dataclasses import dataclass


@dataclass
class Item:
    name: str
    unit_price: float
    quantity: int = 0

    @property
    def total_cost(self):
        return self.unit_price * self.quantity


@dataclass
class Bucket:
    name: str
    items: [Item]

    @property
    def total_cost(self):
        return sum(item.total_cost for item in self.items)
