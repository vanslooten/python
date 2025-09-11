# Define a class Fruit,
# Attributes of Fruit: name, color, price
class Fruit:
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price # in euros

    def info(self):
        return f"Fruit: {self.name}, Color: {self.color}, Price: €{self.price:.2f}" 

# Example usage
if __name__ == "__main__":
    # create instances (objects) of Fruit
    apple = Fruit("Apple", "Red", 0.5) # apple is an object of class Fruit
    banana = Fruit("Banana", "Yellow", 0.3)
    
    # call method info() of the objects:
    print(apple.info())
    print(banana.info())    
