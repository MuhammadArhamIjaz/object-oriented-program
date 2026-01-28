import math

class Circle:
    def __init__(self, radius=None):
        self.radius = radius

    def area(self):
        if self.radius is None:
            return None
        return math.pi * (self.radius ** 2)

    def circumference(self):
        if self.radius is None:
            return None
        return 2 * math.pi * self.radius

    def set_radius_from_area(self, area):
        self.radius = math.sqrt(area / math.pi)

    def set_radius_from_perimeter(self, perimeter):
        self.radius = perimeter / (2 * math.pi)


if __name__ == "__main__":
    # Normal usage
    c = Circle(5)
    print("Radius:", c.radius)
    print("Area:", c.area())
    print("Circumference:", c.circumference())

    # Calculate radius from area
    c2 = Circle()
    c2.set_radius_from_area(78.5)
    print("\nRadius from area:", c2.radius)
    print("Area:", c2.area())

    # Calculate radius from perimeter
    c3 = Circle()
    c3.set_radius_from_perimeter(31.4)
    print("\nRadius from perimeter:", c3.radius)
    print("Circumference:", c3.circumference())
