class Car:
    #инициализатор
    def __init__(self, color, model):
        self.color = color
        self.model = model

    def drive_to_location(self, location):
        print(f'Car {self.model} is driving to {location}')
class Bus(Car):
    def drive_to_location(self, location):
        print(f'Bus {self.model} driving at {location}')
bus_40 = Bus('yellow', 'MERSeDEC BENZO')
bus_40.drive_to_location('bishkek')
print(bus_40)