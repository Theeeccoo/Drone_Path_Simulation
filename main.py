from Grid import Grid
from Client import Client
from Product import Product
from Drone import Drone

# Example execution.

grid = Grid(5, 5)

client1 = Client("Robson", grid.get_position_in_grid(3, 3))
client1.add_product(Product("Laranja", 100.0, 0.5))
client1.add_product(Product("Vasco", 10.0, 0.5))
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

