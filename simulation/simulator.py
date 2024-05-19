def prompt_options():
    print("Please choose one of the following options:")
    print("[1] Add a car to the field")
    print("[2] Run simulation")
    choice = input("Enter your choice: ")
    return choice

def closing_prompt():
    print("Please choose one of the following options:")
    print("[1] Start Over")
    print("[2] Exit")
    choice = input("Enter your choice: ")
    return choice

# def move_car(car, command, board_size, cars):
#     original_x, original_y = car.x, car.y
    
#     if command == 'F':
#         car.move_forward()
#     elif command == 'L':
#         car.rotate_left()
#     elif command == 'R':
#         car.rotate_right()

#     # Check if the new position is within the board boundaries
#     if car.x < 0 or car.x >= board_size[0] or car.y < 0 or car.y >= board_size[1]:
#         car.x, car.y = original_x, original_y  # Revert back to the original position

#     # Check for intersection with other cars
#     for other_car in cars:
#         if other_car != car and car.x == other_car.x and car.y == other_car.y:
#             return (car.x, car.y)  # Return intersection position if found
        
#     return None

# def run_simulation(cars, board_size, cmds):
#     intersections = {}
#     final_steps=0
#     intersect_positions = {}
#     for car in cars:
#         # Retrieve commands for the current car by its name
#         count=0
#         command = cmds.get(car.name)
#         if command is not None:  # Check if commands exist for the car
#             for c in command:
#                 count += 1
#                 intersection = move_car(car, c, board_size, cars)
#                 # print(f"what is the count: {count}")
#                 if intersection:
#                     final_steps=count
#                     intersections[car.name] = intersection
#                     print(f"what is the final_steps: {final_steps}")

#     for car in cars:
#         final_position = intersections.get(car.name, (car.x, car.y))
#         intersect_positions.setdefault(final_position, []).append((car.name, final_steps))
#     return intersect_positions


def move_car(car, command, board_size, cars):
    original_x, original_y = car.x, car.y
    original_direction = car.direction
    
    if command == 'F':
        car.move_forward()
    elif command == 'L':
        car.rotate_left()
    elif command == 'R':
        car.rotate_right()

    # Check if the new position is within the board boundaries
    if car.x < 0 or car.x >= board_size[0] or car.y < 0 or car.y >= board_size[1]:
        car.x, car.y = original_x, original_y  # Revert back to the original position
        car.direction = original_direction
        
    return None

def check_intersection(car, cars):
    for other_car in cars:
        if other_car != car and car.x == other_car.x and car.y == other_car.y:
            return (car.x, car.y)  # Return intersection position if found

    
# test return the pos and check in the main
def run_simulation(cars, board_size, cmds):
    intersections = {}
    pos = {}
    final_steps=0
    intersect_positions = {}
    for car in cars:
        # Retrieve commands for the current car by its name
        count=0
        command = cmds.get(car.name)
        if command is not None:  # Check if commands exist for the car
            for c in command:
                count += 1
                move_car(car, c, board_size, cars)
                intersection = check_intersection(car, cars)
                # print(f"what is the count: {count}")
                if intersection:
                    final_steps=count
                    intersections[car.name] = intersection
                    # print(f"what is the final_steps: {final_steps}")

    for car in cars:
        final_position = intersections.get(car.name, (car.x, car.y))
        intersect_positions.setdefault(final_position, []).append((car.name, final_steps))
    return intersect_positions
