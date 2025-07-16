class SuperVehicle:
    """
    Superclass capturing common state & behavior for any vehicle.
    """

    def __init__(self, name: str, mpg: float) -> None:
        """
        Init function stores the common values shared across all sub functions.
        """

        self.name = name
        self.mpg = mpg  # miles per gallon

    def fuel_needed(self, distance: float) -> float:
        """
        Return how many gallons are needed to travel the given distance.
        """

        return distance / self.mpg

    def description(self) -> str:
        """
        Return a string describing this vehicle's fuel efficiency.
        """

        return f"{self.name} gets {self.mpg} miles per gallon."


class Car(SuperVehicle):
    def __init__(self) -> None:
        super().__init__("Car", 30)


class Truck(SuperVehicle):
    def __init__(self) -> None:
        super().__init__("Truck", 15)


class Motorcycle(SuperVehicle):
    def __init__(self) -> None:
        super().__init__("Motorcycle", 50)


class Bus(SuperVehicle):
    def __init__(self) -> None:
        super().__init__("Bus", 8)


# Custom testing
car        = Car()
truck      = Truck()
motorcycle = Motorcycle()
bus        = Bus()

print(car.fuel_needed(150)) # 5.0
print(truck.fuel_needed(150)) # 10.0
print(motorcycle.fuel_needed(150)) # 3.0
print(bus.fuel_needed(150)) # 18.75
print(car.fuel_needed(0)) # 0.0
print(motorcycle.fuel_needed(-100))#  -2.0
print(car.description()) # "Car gets 30 miles per gallon."
print(truck.description()) # "Truck gets 15 miles per gallon."
print(motorcycle.description()) # "Motorcycle gets 50 miles per gallon."
print(bus.description()) # "Bus gets 8 miles per gallon."


#--------------------------------------------------------------------------------#
# ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎  WRITE YOUR CODE ABOVE THIS  LINE ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓  IF THERE IS ANY CODE BELOW THIS LINE ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓         PLEASE DO NOT MODIFY IF       ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
#--------------------------------------------------------------------------------#
# 