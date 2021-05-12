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

    @property
    def receipt(self):
        s = 'Item, Unit Price, Quality, Total Cost'

        if self.items:
            for item in self.items:
                s += f'{item.name}, {item.unit_price}, {item.quantity}, {item.total_cost}'

            s += f'----,----,----,{self.total_cost}'
            return s
        raise Exception("Can't create receipt without data")
