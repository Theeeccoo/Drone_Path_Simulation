from Grid import Grid
from Client import Client
from Product import Product
from Drone import Drone
from Order import Order
from queue import PriorityQueue
import os
import platform

grid = Grid(5, 5)

# Drone's base coords
X_base = 2
Y_base = 2

clients = []
orders = []
drones = []

def clear_terminal():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def build():

    with open('./archives/drones.txt', 'r') as arquivo:
        for line in arquivo: 
            maximum_altitude, maximum_weight, maximum_velocity = map(float, line.split(' ')) 
            current_drone = Drone(maximum_altitude, maximum_weight, maximum_velocity)
            current_drone.set_current_position(grid.get_position_in_grid(X_base, Y_base))
            drones.append(current_drone)


    for drone in drones:
        print(drone.id)

    base_position = grid.get_position_in_grid(X_base, Y_base)
    base_position.set_position_classification("base")

    with open('./archives/clients1.txt', 'r') as arquivo:
        for line in arquivo:
            name, positions = line.strip().split(',')  
            x, y = map(int, positions.split()) 
            client_position = grid.get_position_in_grid(x, y)
            client_position.set_position_classification("client")
            clients.append(Client(name, client_position))


    for client in clients:
        print(client)

    with open('./archives/orders1.txt', 'r') as arquivo:
        for line in arquivo:
            parts = line.strip().split(',')
            client_name = parts[0] 
            products = parts[1:]

            # Check if client exists
            client = next((client for client in clients if client.name == client_name), None)
            if client == None:
                raise ValueError("ERROR in build. Your client does not exist.")

            products_list = []
            for product in products:
                product_name, price, weight = product.split()
                price = float(price)  
                weight = float(weight)    

                # Add products to the customer's product list
                new_product = Product(product_name, price, weight)
                client.add_product(new_product)

                products_list.append(new_product)

            orders.append(Order(client, products_list))
            
    for client in clients:
        print(client)

def manhattan_distance(node, goal):
    return abs(node.X - goal.X) + abs(node.Y - goal.Y)

def a_star(start, goal, drone):
    open_set = PriorityQueue()
    open_set.put((0, start.X, start.Y, start))
    came_from = {}

    g_score = {position: float('inf') for position in grid.positions}
    g_score[start] = 0
    f_score = {position: float('inf') for position in grid.positions}
    f_score[start] = manhattan_distance(start, goal)

    while not open_set.empty():
        _, _, _, current = open_set.get()

        # Client found
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]
        
        #cost = distance / speed + battery_consumption(distance, altitude, weight)
        for neighbor in grid.get_neighbors(current):
            distance = manhattan_distance(current, neighbor)
            altitude = neighbor.Z
            weight = drone.current_weight
            velocity = drone.update_drone_velocity()
            cost = distance / velocity

            if g_score[current] + cost < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = g_score[current] + cost
                f_score[neighbor] = g_score[neighbor] + manhattan_distance(neighbor, goal)
                open_set.put((f_score[neighbor], neighbor.X, neighbor.Y, neighbor))

def battery_consumption(distance, altitude, weight, velocity):
    """
    Calculates battery consumption. It is defined by the function b -= distance * (base_consumption + altitude_factor + weight_factor)
    distance = manhattan_distance between initial an final point
    base_consumption = 0.1 per grid
    altitude_factor = 0.0001 * altitude
    weight_facotr = 0.02 * weight
    """
    base_consumption = 10
    altitude_factor = 0.0001 * altitude
    weight_factor = 0.1 * weight
    return (distance / velocity) * (base_consumption + altitude_factor + weight_factor)

def calculate_battery_for_route(route, weight, velocity):
    total_battery_consumed = 0
    for i in range(len(route) - 1):
        current = route[i]
        next_node = route[i + 1]
        distance = manhattan_distance(current, next_node)
        altitude = current.Z
        total_battery_consumed += battery_consumption(distance, altitude, weight, velocity)
    return total_battery_consumed

def find_best_route_with_battery_check(start_position, client_position, base_position, drone, order_weight, more_orders):

    went_to_recharge = False

    # If drone hasn't finished it's orders
    if not more_orders:
        # Find best route to client
        route_to_client = a_star(start_position, client_position, drone)
        battery_consumption = calculate_battery_for_route(route_to_client, drone.current_weight, drone.velocity)
        route_to_base = a_star(client_position, base_position, drone)
        battery_consumption += calculate_battery_for_route(route_to_base, (drone.current_weight - order_weight), drone.velocity)
        final_route = route_to_client

        visual_string = f"Current total battery: {(drone.battery / drone.maximum_battery ) * 100:.2f}%\nWill consume {(battery_consumption / drone.maximum_battery) * 100:.2f}% to next route\n"
        # If route taken consumes more battery than drone has or will make it get stuck, we must send drone to base to recharge
        if ( battery_consumption > drone.battery ):
            went_to_recharge = True
            final_route = a_star(drone.current_position, base_position, drone)
            battery_consumption = calculate_battery_for_route(final_route, drone.current_weight, drone.velocity)

        if went_to_recharge: visual_string += "Going back to base to recharge!\n"
        print(visual_string)
        for position in final_route:
            drone.set_current_position(position)
            position.set_position_classification("drone")
            print(grid)
            foo = input("Next step...")
            clear_terminal()
            grid.grid_update_position_classification()

        if (went_to_recharge):
            drone.update_drone_battery(drone.maximum_battery)
        else:
            drone.update_drone_battery(drone.battery - battery_consumption)


    else:
        print("Going back to get more orders.")
        route_to_base = a_star(start_position, client_position, drone)
        battery_consumption = calculate_battery_for_route(route_to_base, drone.current_weight, drone.velocity)
        for position in route_to_base:
            drone.set_current_position(position)
            position.set_position_classification("drone")
            print(grid)
            foo = input("Next step...")
            clear_terminal()
            grid.grid_update_position_classification()

        drone.update_drone_battery(drone.maximum_battery)


    return went_to_recharge


def main():
    build()

    clear_terminal()
    print(grid)
    foo = input("Next step...")
    clear_terminal()

    # Add new order in drone
    while len(orders) > 0 :
        iterator = 0    
        next_drone = drones[0]

        # Adding all orders in drone. 
        # Iterating through orders and making sure that the order's weight won't surpass drone's maximum weight
        while iterator < len(orders):
            next_order = orders[iterator]
            next_weight = next_drone.current_weight + next_order.total_weight

            if ( next_weight <= next_drone.maximum_weight ):
                next_drone.add_new_order(next_order)
                orders.remove(next_order)
            else:
                iterator += 1

        while len(next_drone.get_orders()) > 0:
            orders_to_be_processed = next_drone.get_orders()
            
            client = next(iter(orders_to_be_processed))
            products = orders_to_be_processed[client]

            order_weight = sum(product.weight for product in products)

            went_to_recharge = find_best_route_with_battery_check(next_drone.current_position, client.position, grid.get_position_in_grid(X_base, Y_base), next_drone, order_weight, False)

            if not went_to_recharge:
                del next_drone.get_orders()[client]


        next_drone.clear_orders()
        
        find_best_route_with_battery_check(next_drone.current_position, grid.get_position_in_grid(X_base, Y_base), grid.get_position_in_grid(X_base, Y_base), next_drone, order_weight, True)



if __name__ == "__main__":
    main()