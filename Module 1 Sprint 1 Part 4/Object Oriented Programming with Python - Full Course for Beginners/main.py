class Item:
    pay_rate = 0.8 #Class attribute. Means 20% discount
    def __init__(self, name: str, price: float , quantity = 0):
        # RUn validations to the received arguments
        assert price  >= 0, f"Price {price} is not greater than zero"
        assert quantity >= 0, f"Price {quantity} is not greater than zero"

        # Assign to self object. Instance attributes:
        self.price = price
        self.name = name
        self.quantity = quantity
        
    def calculate_total_price(self): #this is method not a function if in CLASS
        return self.price * self.quantity
    def apply_discount(self):
        self.price = self.price * self.pay_rate

item1 = Item('Phone', 100, 1)
item2 = Item('Laptop', 1000, 3)

print(Item.__dict__) # All the attributes for Class level
print(item1.__dict__) # All the attributes for Instance level


