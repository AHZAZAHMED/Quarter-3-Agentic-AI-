from typing import Callable
from dataclasses import dataclass

@dataclass
class Math:
    operation : Callable[[int,int], str]

    def apply_operation(self, a: int, b:int) -> str:
        return self.operation(a,b)

def add(a:int,b:int)->str:
    return f"Sum of two number is:{a+b}"

def subtract(a:int,b:int)->str:
    return f"subtraction of two number is:{a-b}"

def mutiply(a:int,b:int) -> str:
    return f"Multiplication of two number is:{a*b}"

addition = Math(operation = add)
print(addition.apply_operation(10,5))

subtraction = Math(operation = subtract)
print(subtraction.apply_operation(10,5))

multiplication = Math(operation = mutiply)
print(multiplication.apply_operation(10,5))