from math import pi


def circle_area(radius):
  if type(radius) not in [int, float] :
    raise TypeError("Radius cannot be a string, complex or boolean")
  if radius < 0 :
    raise ValueError("The radius cannot be negative or a string or complex")
  return round((pi * radius**2), 6)

