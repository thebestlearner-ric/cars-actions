from simulation.simulator import run_simulation
from simulation.simulator import prompt_options, closing_prompt
from cars.cars import Car

def main():
    while True:
        print("Welcome to Auto Driving Simulation")
        board_size_input = input("Enter the size of the board (X Y): ")
        x_size, y_size = map(int, board_size_input.split())
        board_size = (x_size, y_size)
        cars = []
        commands = {}  # Store commands for each car
        while True:
            choice = prompt_options()
            if choice == '1':
                name = input("Enter the name of the car: ")
                car_init_position = input(f"Please enter initial position of car {name} in x y Direction format: ")
                x, y, direction = map(str, car_init_position.split())
                commands[name] = input(f"Enter the commands for car {name}: ").upper()  # Store commands for the car
                cars.append(Car(name, direction.upper(), int(x), int(y)))
                # Print current list of cars with their commands
                print("Current list of cars:")
                for car in cars:
                    print(f"- {car.name}, ({car.x}, {car.y}) {car.direction}, {commands[car.name]}")
            elif choice == '2':
                intersect_positions = run_simulation(cars, board_size, commands)  # Pass commands to the run_simulation function
                # print(f"{intersect_positions}")
                print("After simulation, the result is:")
                for position, cars_at_position in intersect_positions.items():
                    if len(cars_at_position) > 1:
                        # Extract car names and final steps
                        car_info = [(car[0], car[1]) for car in cars_at_position]
                        for i in range(len(car_info)):
                            if i < len(car_info) - 1:
                                car1, final_step1 = car_info[i]
                                car2, final_step2 = car_info[i + 1]
                                print(f"- {car1}, collides with {car2} at {position} at {final_step1}")
                                print(f"- {car2}, collides with {car1} at {position} at {final_step2}")
                    else:
                        for car in cars:
                            print(f"- {car.name}, ({car.x}, {car.y}) {car.direction}")
                closing_choice = closing_prompt()
                if closing_choice == '1':
                    break
                elif closing_choice == '2':
                    return
                else:
                    print("Invalid choice. Please choose again.")
            else:
                print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
