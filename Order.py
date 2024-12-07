class Order:
    """
    Order Class.

    Attributes:
        client_name         (str): Client name.
        products            (list[Products]): Product's client order.
        accumulate_weight   (float): Cumulative order weight.
    """

    def __init__(self, client_name, products):
        """
        Initiates a new Order instance with specified values. Null or invalid values are considered as an error (raises ValueError).

        Args:
            client_name     (str): Client name.
            products        (list[Products]): Product's client order.

        Raises:
            ValueError: If attributes "client_name", "products" are either None or invalid (Empty string, negative values or incorrect Type).
            TypeError: If attributes "client_name", "products" have incorrect types.

        """

        # Sanity Check #
        if (client_name is None) or (client_name == ""):
            raise ValueError("ERROR in __init__ in Order. Your Order must have a valid client name.")
        if (not isinstance(client_name, str)):
            raise TypeError("ERROR in __init__ in Order. Your Client name must be an instance of str.")

        if ( len(products) == 0 ):
            raise ValueError("ERROR in __init__ in Order. Your order must have atleast one Product to make an order.")


        self.client_name = client_name
        self.products = products

        self.accumulate_weight = 0.0
        for product in products:
            self.accumulate_weight += product.weight

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

        return_string = f"{self.client_name}:\n"
        return_string += "   Product:    Name                 Price               Weight\n"
        for product in self.products:
            return_string += f"\t{str(product)}\n"
        return return_string