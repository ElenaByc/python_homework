import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def distance_to(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


class Vector(Point):
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented


# Demonstrate all classes and methods
if __name__ == "__main__":
    # Create some points
    p1 = Point(1, 2)
    p2 = Point(4, 6)
    p3 = Point(1, 2)

    print("Point class demonstrations:")
    print(f"p1 = {p1}")
    print(f"p2 = {p2}")
    print(f"p3 = {p3}")
    print(f"p1 == p2: {p1 == p2}")
    print(f"p1 == p3: {p1 == p3}")
    print(f"Distance from p1 to p2: {p1.distance_to(p2):.2f}")
    print(f"Distance from p1 to p3: {p1.distance_to(p3):.2f}")
    print()

    # Create some vectors
    v1 = Vector(3, 4)
    v2 = Vector(1, 2)
    v3 = Vector(5, 6)

    print("Vector class demonstrations:")
    print(f"v1 = {v1}")
    print(f"v2 = {v2}")
    print(f"v3 = {v3}")
    print(f"v1 + v2 = {v1 + v2}")
    print(f"v2 + v3 = {v2 + v3}")
    print()

    # Demonstrate that Vector inherits methods from Point
    print("Vector inherits Point methods:")
    print(f"v1 == v2: {v1 == v2}")
    print(f"Distance from v1 to v2: {v1.distance_to(v2):.2f}")
