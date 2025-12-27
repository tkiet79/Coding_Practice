import math
AB = float(input())
BC = float(input())

sin_a = AB / (math.sqrt(AB**2 + BC**2))
a_rad = math.asin(sin_a)
a_degree = round(math.degrees(a_rad))
print(f"{a_degree:.0f}\u00B0")