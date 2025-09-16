class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model
        self._fined = False
    def drive_to_location(self, location):
        print(f"Car {self.model} is driving to {location}")
    def _test_car(self):
        print(f"test car {self.model}")
car_honda = Car('black', 'Honda Civic')
print(car_honda._fined)
car_honda._test_car()
@property
def color(self):
    return self.color
print(car_honda.color)