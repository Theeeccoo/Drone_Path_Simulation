class Product:
    """
    Product Class.

    Attributes:
        name     (str): Product's name.
        price  (float): Product's total price.
        weight (float): Product's total weight.
    """

    def __init__(self, name, price, weight):
        """
        Initiates a new Product instance with specified values. Null or invalid values are considered as an error (raises ValueError).

        Args:
            name     (str): Product's name.
            price  (float): Product's total price.
            weight (float): Product's total price.

        Raises:
            ValueError: If attributes "name", "price", "weight" are either None or invalid (Empty string, negative values or incorrect Type).
            TypeError: If attributes "name", "price", "weight" have incorrect types.

        """

        # Sanity Check #
        if (name is None) or (name == ""):
            raise ValueError("ERROR in __init__ in Product. Your Product must have a valid name.")
        if (not isinstance(name, str)):
            raise TypeError("ERROR in __init__ in Product. Your Product's name must be an instance of str.")

        if (price is None) or (price < 0.0):
            raise ValueError("ERROR in __init__ in Product. Your Product must have a valid price.")
        if (not isinstance(price, float)):
            raise TypeError("ERROR in __init__ in Product. Your Product's price must be an instance of float.")

        if (weight is None) or (weight < 0.0):
            raise ValueError("ERROR in __init__ in Product. Your Product must have a valid weight.")
        if (not isinstance(weight, float)):
            raise TypeError("ERROR in __init__ in Product. Your Product's weight must be an instance of float.")


        self.name = name
        self.price = price
        self.weight = weight

    def get_product_info(self):
        """
        Gets Product's attributes.

        Returns:
            dict: Product's attributes as a dictionary.
        """
        return self.__dict__

    def __str__(self):
        """
        Returns stringfied representation of a Product instance.

        Returns:
            str: Stringfied representation of a Product instance.
        """

        return f"{self.name:^20} {self.price:^20} {self.weight:^20}"

