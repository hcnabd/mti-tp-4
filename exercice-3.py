# The `Square` class inherits from `Rectangle` but overrides `set_width` and `set_height` to keep width and height equal. This breaks the Liskov Substitution Principle (LSP) because code expecting a `Rectangle` may behave incorrectly when given a `Square`.

class Rectangle:
        def set_width(self, width):
                self._width = width

        def set_height(self, height):
                self._height = height

class Square(Rectangle):
        def set_width(self, width):
                self._width = width
                self._height = width # Violation!

        def set_height(self, height):
                self._width = height
                self._height = height

def test_area(rect: Rectangle):
    rect.set_width(5)
    rect.set_height(10)
    area = rect._width * rect._height
    assert area == 50, f"Expected area 50, got {area}"

rect = Rectangle()
test_area(rect)  # Passes

square = Square()
test_area(square)  # Fails, area = 100, not 50

# Clients expecting a Rectangle behavior cannot substitute a Square without unexpected results. The child class changes the expected behavior of the parent.

# ------------------------------------------------------------

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

# ------------------------------------------------------------

from abc import ABC, abstractmethod

class Bird(ABC):
    @abstractmethod
    def move(self):
        pass

class FlyingBird(Bird):
    def move(self):
        print("I fly!")

class Penguin(Bird):
    def move(self):
        print("I swim!")
