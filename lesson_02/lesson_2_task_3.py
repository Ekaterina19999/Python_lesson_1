import math


def square(side):

    area = side * side

    return math.ceil(area)



print(f"Сторона 5, площадь: {square(5)}")

print(f"Сторона 4.1, площадь: {square(4.1)}")

