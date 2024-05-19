import unittest
from cars.cars import Car

class TestCarMethods(unittest.TestCase):
    def test_move_forward(self):
        car = Car("Test", "N", 0, 0)
        car.move_forward()
        self.assertEqual(car.y, 1)  # Check if the car moved forward correctly
        print("test_car moves Forward")

    def test_rotate_left(self):
        car = Car("Test", "N", 0, 0)
        car.rotate_left()
        self.assertEqual(car.direction, "W")  # Check if the car rotated left correctly
        print("test_car turns rotates 90 left")

    def test_rotate_right(self):
        car = Car("Test", "N", 0, 0)
        car.rotate_right()
        self.assertEqual(car.direction, "E")  # Check if the car rotated right correctly
        print("test_car turns rotates 90 right")

if __name__ == '__main__':
    unittest.main()
