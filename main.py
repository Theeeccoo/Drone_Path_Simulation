from Grid import Grid
from Client import Client
from Product import Product
from Drone import Drone

grid = Grid(5, 5)
client1 = Client("Robson", grid.get_position_in_grid(3, 3))
client1.add_product(Product("Laranja", 100.0, 0.5))
client1.add_product(Product("Vasco", 10.0, 0.5))
products = client1.products
for product in products:
    print(product.get_product_info())

drone = Drone(1000.0, 1000.0, 1000.0)
drone.get_order(client1)
print(drone.get_drone_info())
client1.add_product(Product("Mouse", 1000.0, 0.2))
drone.get_order(client1)
print(drone.get_drone_info())

client2 = Client("Jandira", grid.get_position_in_grid(2, 1))
client2.add_product(Product("Pamonha", 100.0, 0.5))
drone.get_order(client2)

# Example: Getting Client from Order
keys = list(drone.get_drone_info()["order"].keys())
client_info = keys[keys.index(client2)].get_client_info()
print(client_info)
# Example: Getting Product from Order
print(drone.get_drone_info()["order"].get(client2)[0].get_product_info())
