from dataclasses import dataclass , field
from typing import Generic, TypeVar
from dataclass import Product

T= TypeVar('T')
@dataclass
class Stack(Generic[T]):
    items: list[T] = field(default_factory=list)
    
    def push(self,item: T) -> None:
        return self.items.append(item)
    
    def pop(self) -> T:
        if not self.items:
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self , index: int) -> T:
        if not self.items:
            raise IndexError("peek from empty stack")
        return self.items[index]

# Stack class working with different types

#integer stack
stack_int = Stack[int]()
stack_int.push(1)
stack_int.push(2)
print(stack_int.items)
stack_int.pop()
print(stack_int.peek(-1))

# string stack
stack_str = Stack[str]()
stack_str.push("ali")
print(stack_str.items)

#Product Stack
stack_product = Stack[Product]()
stack_product.push(Product(name="phone", price=50000.0 , quantity=3))
print(stack_product.items)
top_product = stack_product.peek(-1)
print(f"Top product total price: {top_product.calculate()}")