from Grid import Grid
from Client import Client
from Product import Product
from Drone import Drone
from Order import Order

# Example execution.

grid = Grid(5, 5)
print(grid)

# Base coords of drone
X_base = 2
Y_base = 2

clients = []
orders = []
drones = []

with open('./archives/drones.txt', 'r') as arquivo:
    for line in arquivo: 
        maximum_altitude, maximum_weight, maximum_velocity = map(float, line.split(' ')) 
        drones.append(Drone(maximum_altitude, maximum_weight, maximum_velocity))

for drone in drones:
    print(drone.id)

with open('./archives/clients1.txt', 'r') as arquivo:
    for line in arquivo:
        name, positions = line.strip().split(',')  
        x, y = map(int, positions.split()) 
        clients.append(Client(name, grid.get_position_in_grid(x, y)))

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
            raise ValueError("ERROR in main in read orders. Your client not exist.")

        products_list = []
        for product in products:
            product_name, price, weight = product.split()
            price = float(price)  
            weight = float(weight)    

            # Add products to the customer's product list
            client.add_product(Product(product_name, price, weight))

            products_list.append(Product(product_name, price, weight))

        orders.append(Order(client_name, products_list))
        
print(f"len order: {len(orders)}")
print(drone.get_drone_info())

for client in clients:
    print(client)

# Add new order in drone
for order in orders:
    if drone

""" 
# Add new order in drone
    drone.add_new_order(client)
client1.add_product(Product("Laranja", 100.0, 0.5))
client1.add_product(Product("Vasco", 10.0, 0.5))
print(client1)
products = client1.products
for product in products:
    print(product.get_product_info())

drone = Drone(1000.0, 1000.0, 1000.0)
drone.add_new_order(client1)
print(drone.get_drone_info())

client1.add_product(Product("Mouse", 1000.0, 0.2))
drone.add_new_order(client1)
print(drone.get_drone_info())

client2 = Client("Jandira", grid.get_position_in_grid(2, 1))
client2.add_product(Product("Pamonha", 100.0, 0.5))
drone.add_new_order(client2)

client3 = Client("Cleonildo", grid.get_position_in_grid(4, 4))

# Change client to check differences in results
return_order = drone.get_order(client3)
if (return_order is not None):
    [(return_client, return_products)] = return_order.items()
    print(f"Client: {return_client.get_client_info()["name"]}\nProducts:")
    for return_product in return_products:
        info = return_product.get_product_info()
        print(f"\t{info["name"]} <> {info["price"]} <> {info["weight"]}")
else:
    print(f"Client {client3.get_client_info()["name"]} has no orders in drone {drone.get_drone_info()["id"]}")

"""