import datetime

class Car(object):
    current_year: int = datetime.datetime.now().year  # Class attribute for the current year

    def __init__(self, maker: str, model: str, year: int, orig_car_price: float):
        """
        Initializes a Car instance with the provided attributes.
        """
        self.maker = maker
        self.model = model
        self.year = year
        self.orig_car_price = orig_car_price

    def age(self) -> int:
        """
        Calculates the age of the car.
        """
        return self.current_year - self.year
    
    def current_value(self) -> float:
        """
        Calculates the current value of the car based on depreciation.
        """
        depreciation_rate = 0.15
        depreciation_amount = self.orig_car_price * depreciation_rate * self.age()
        current_price = self.orig_car_price - depreciation_amount
        return max(current_price, 0)
    
    def features(self):
        """
        Displays the features of the car including the current value.
        """
        print(f"Maker: {self.maker}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Original Price: {self.orig_car_price}€")
        print(f"Current Value: {self.current_value()}€")
    

car1 = Car("Toyota", "Corolla", 2018, 20000)
car2 = Car("Honda", "Civic", 1995, 35000)

car1.features()
print("-" * 35)
car2.features()
