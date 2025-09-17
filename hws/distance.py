class Distance():
    def __init__(self, value, unit = 'm'):
        units = {
            "mm": 0.001,
            "cm": 0.01,
            "m": 1,
            "km": 1000
        }
        self.value = value
        self.unit = unit
    def to_meters(self):
        return self.value * self.units[self.unit]
    def __str__(self):
        return f'{self.value}, {self.unit}'
    def __add__(self, other):
        total_m = self.to_meters() + other.to_meters
        return total_m(self.value + other.value)
    def __sub__(self, other):
        diff_m = self.to_meters() - other.to_meters()
        if diff_m < 0:
            print("Результат не может быть отрицательным")
        return Distance(self.value - other.value)
    




