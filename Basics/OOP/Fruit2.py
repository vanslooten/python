# Define a dataclass Fruit,
# Attributes of Fruit: name, color, price
from dataclasses import dataclass

@dataclass
class Fruit():
    name: str
    color: str
    price: float

# Example usage
if __name__ == "__main__":
    # create instances (objects) of Fruit
    apple = Fruit("Apple", "Red", 0.5) # apple is an object of class Fruit
    banana = Fruit("Banana", "Yellow", 0.3)
    
    # print info of the objects:
    print(apple)
    print(banana)    
