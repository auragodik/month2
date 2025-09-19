class Distance:
    units = {
        "mm": 0.001,
        "cm": 0.01,
        "m": 1,
        "km": 1000
    }

    def __init__(self, value, unit="m"):
        self.value = value
        self.unit = unit

    def to_meters(self):
        return Distance(self.value * self.units[self.unit], "m")

    def __str__(self):
        return f"{self.to_meters().value} m"

    def __add__(self, other):
        total_m = self.to_meters().value + other.to_meters().value
        return Distance(total_m / Distance.units[self.unit], self.unit)

    def __sub__(self, other):
        diff_m = self.to_meters().value - other.to_meters().value
        if diff_m < 0:
            raise ValueError("Результат не может быть отрицательным")
        return Distance(diff_m / Distance.units[self.unit], self.unit)

