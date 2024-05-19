import unittest
from simulation.simulator import run_simulation, move_car
from cars.cars import Car

class TestCar(unittest.TestCase):
    def test_move_forward_N(self):
        car = Car('test_car', 'N', 0, 0)
        car.move_forward()
        self.assertEqual((car.x, car.y), (0, 1))

    def test_move_forward_S(self):
        car = Car('test_car', 'S', 0, 0)
        car.move_forward()
        self.assertEqual((car.x, car.y), (0, -1))

    # Add similar tests for other directions and for other methods like rotate_left and rotate_right

class TestMoveCar(unittest.TestCase):
    def test_move_car(self):
        car = Car('test_car', 'N', 0, 0)
        board_size = (5, 5)
        other_car = Car('other_car', 'N', 1, 0)
        intersection = move_car(car, 'F', board_size, [other_car])
        self.assertIsNone(intersection)
        self.assertEqual((car.x, car.y), (0, 1))

    # Add more tests for different scenarios including boundary conditions and intersections

class TestRunSimulation(unittest.TestCase):
    def test_run_simulation_single(self):
        cars = []
        # Define the test parameters
        car_A = Car("car_A", "N", 1, 2)
        board_size = (10, 10)
        cmds = {"car_A": "FFRFFFFRRL"}
        cars.append(car_A)
        # Run the simulation
        intersect_positions = run_simulation(cars, board_size, cmds)
        
        # Assert the expected results
        expected_result = {(5, 4): [('car_A', 0)]}
        self.assertEqual(intersect_positions, expected_result)
    
    def test_run_simulation_multiple(self):
        cars = []
        # Define the test parameters
        car_A = Car("car_A", "N", 1, 2)
        car_B = Car("car_B", "W", 7, 8)
        board_size = (10, 10)
        cmds = {"car_A": "FFRFFFFRRL", "car_B": "FFLFFFFFFF"}
        cars.append(car_A)
        cars.append(car_B)
        # Run the simulation
        intersect_positions = run_simulation(cars, board_size, cmds)
        
        # Assert the expected results
        expected_result = {(5, 4): [('car_A', 7), ('car_B', 7)]}
        self.assertEqual(intersect_positions, expected_result)

if __name__ == '__main__':
    unittest.main()
