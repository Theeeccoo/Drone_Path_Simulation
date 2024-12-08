from Client import Client

class Order:
    """
    Order Class.

    Attributes:
        client          (Client): Order's client.
        products        (list[Products]): Order's products.
        total_weight    (float): Order's total weight.
    """

    def __init__(self, client, products):
        """
        Initiates a new Order instance with specified values. Null or invalid values are considered as an error (raises ValueError).

        Args:
            client      (Client): Order's client.
            products    (list[Products]): Order's products.

        Raises:
            ValueError: If attributes "client", "products" are either None or invalid (empty list or incorrect Type).
            TypeError: If attributes "client", "products" have incorrect types.

        """

        # Sanity Check #
        if (client is None):
            raise ValueError("ERROR in __init__ in Order. Your Order must be valid.")
        if (not isinstance(client, Client)):
            raise TypeError("ERROR in __init__ in Order. Your Client must be an instance of Client.")
            
        if ( len(products) == 0 ):
            raise ValueError("ERROR in __init__ in Order. Your order must have atleast one Product to make an order.")


        self.client = client
        self.products = products

        self.total_weight = 0.0
        for product in products:
            self.total_weight += product.weight

    def get_order_info(self):
        """
        Gets Order's attributes.

        Returns:
            dict: Order's attributes as a dictionary.
        """
        return self.__dict__

    def __str__(self):
        """
        Returns stringfied representation of a Order instance.

        Returns:
            str: Stringfied representation of a Order instance.
        """

        return_string = f"{self.client.name}:\n"
        return_string += f"Total order's weight: {self.total_weight}\n"
        return_string += "   Product:    Name                 Price               Weight\n"
        for product in self.products:
            return_string += f"\t{str(product)}\n"
        return return_string