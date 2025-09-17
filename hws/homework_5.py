from homeworks.distance import Distance

d1 = Distance(100, "m")
d2 = Distance(2, "km")
d3 = Distance(50, "cm")

print(d1)       # 100 m
print(d2)       # 2 km
print(d3)       # 50 cm

print(d1 + d2)  # 2100 m
print(d2 - d1)  # 1900 km