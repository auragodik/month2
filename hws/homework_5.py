from hws.distance import Distance

d1 = Distance(100, "m")
d2 = Distance(2, "km")
d3 = Distance(50, "cm")

print(d1)
print(d2)
print(d3)

print(d1 + d2)
print(d2 - d1)