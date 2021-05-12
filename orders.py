from dataclasses import dataclass


@dataclass
class Order:
    name: str
    unit_price: float
    quantity: int = 0

    @property
    def total_cost(self):
        return self.unit_price * self.quantity
