from Product import Product
from Grid import Position
class Client:
    """
    Client class.

    Attributes:
        name                (str): Client's name.
        position       (Position): Client's grid Position (XY).
        products (list[Products]): Client's Product.
    """

    def __init__(self, name, position):
        """
        Initiates a new Client instance with specified values. Null or invalid values are considered as an error (raises ValueError or TypeError).

        Args:
            name          (str): Client's name.
            position (Position): Client's grid Position (XY).

        Raises:
            ValueError: If attributes "name", "position" are either None or invalid (Empty string).
            TypeError: If attributes "name", "position" have incorrect types.
        """

        # Sanity Check #
        if (name is None) or (name == ""):
            raise ValueError("ERROR in __init__ in Client. Your Client must have a valid name.")
        if not isinstance(name, str):
            raise TypeError("ERROR in __init__ in Client. Your Client's name must be an instance of str.")
        if (position is None):
            raise ValueError("ERROR in __init__ in Client. Your Client must have a valid position.")
        if not isinstance(position, Position):
            raise TypeError("ERROR in __init__ in Client. Your Client's position must be an instance of Position.")
        

        self.name = name
        self.position = position
        self.products = []

    def add_product(self, product):
        """
        Adds a new Product to Client.

        Args:
            product (Product): New added Product.

        Raises:
            TypeError: If "product" is not an instance of Product.
        """
        if isinstance(product, Product):
            self.products.append(product)
        else: 
            raise TypeError("ERROR in add_product in Client. Only Product instances can be added to Client.")

    def get_products(self):
        """
        Returns Client's Products.

        Returns:
            list[Product]: List of all Client's Products' attributes.
        """
        return self.products
    
    def get_client_info(self):
        """
        Gets Client's attributes.

        Returns:
            dict: Client's attributes as a dictionary.
        """
        return self.__dict__





