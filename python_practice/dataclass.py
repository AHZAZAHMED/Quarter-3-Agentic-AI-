from typing import Generic , ClassVar ,TypeVar 
from dataclasses import dataclass ,field

@dataclass
class Product:
    name: str
    price: float
    quantity: int

    def calculate(self)-> float:
        return self.price * self.quantity


#Inventory class
@dataclass
class Inventory:
    products: list[Product] = field(default_factory=list)

    def add_product(self, product:Product) -> None:
        self.products.append(product)

    def total_inventory_value(self) -> float:
        return sum(product.calculate() for product in self.products)

inventory1 = Inventory()
product = Product(name="laptop", price=100000.0, quantity=3)
inventory1.add_product(product)
print(inventory1.total_inventory_value())

