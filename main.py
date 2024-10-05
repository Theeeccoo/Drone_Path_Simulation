from Grid import Grid
from Client import Client
from Product import Product

grid = Grid(5, 5)
client1 = Client("Robson", grid.get_position_in_grid(3, 3))
client1.add_product(Product("Laranja", 100.00, 0.5))
client1.add_product(Product("Vasco", 1000000000.00, 0.5))
products = client1.get_products()
for product in products:
    print(product.get_product_info())
