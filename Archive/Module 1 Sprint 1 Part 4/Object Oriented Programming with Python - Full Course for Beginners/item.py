import csv

class Item:
    pay_rate = 0.8 #Class attribute. Means 20% discount
    all = []
    def __init__(self, name: str, price: float , quantity = 0):
        # Run validations to the received arguments
        assert price  >= 0, f"Price {price} is not greater than zero"
        assert quantity >= 0, f"Price {quantity} is not greater than zero"

        # Assign to self object. Instance attributes:
        self.price = price
        self.__name = name
        self.quantity = quantity

        # Actions to execute:
        Item.all.append(self)
    @property
    # Property Decorator = Attribute read-only
    def name(self):
        return self.__name  

    @name.setter
    def name(self, value):
        self.__name = value  


    def calculate_total_price(self): #this is method not a function if in CLASS
        return self.price * self.quantity
    def apply_discount(self):
        self.price = self.price * self.pay_rate
    
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity')),
            )
    @staticmethod        
    def is_integer(num):
        #We will count out the floats that are point zero
        if isinstance(num, float):
            # Count the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False


    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"