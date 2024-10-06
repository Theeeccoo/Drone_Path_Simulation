from Product import Product
from Grid import Position
from Client import Client

from collections import defaultdict

class Drone:
    """
    Drone class.

    Attributes:
        id                                       (int): Drone's IDentification number.
        altitude                               (float): Drone's current altitude.
        maximum_altitude                       (float): Drone's maximum altitude.
        batery                                 (float): Drone's current batery.
        current_position                    (Position): Drone's current grid Position (XY).
        current_weight                         (float): Drone's current weight.
        maximum_weight                         (float): Drone's maximum weight.
        orders           (dict{Client: list[Product]}): Drone's dictionary of Clients orders.
        path                          (list[Position]): Drone's path at given moment.
        velocity                               (float): Drone's current velocity.
        maximum_velocity                       (float): Drone's maximum velocity.
    """
    # Class shared variable
    _id_counter = 1

    def __init__(self, maximum_altitude, maximum_weight, maximum_velocity):
        """
        Initiates a new Drone instance with specified values. Null or invalid values are considered as an error (raises ValueError or TypeError).

        Args:
            maximum_altitude (float): Drone's maximum altitude.
            maximum_weight   (float): Drone's maximum weight.
            maximum_velocity (float): Drone's maximum velocity.

        Raises: 
            ValueError: If attributes "maximum_altitude", "maximum_weight", "maximum_velocity" are either None or invalid (Negative values).
            TypeError: If attributes "maximum_altitude", "maximum_weight", "maximum_velocity" have incorrect types.
        """

        # Sanity Check #
        if (maximum_altitude is None) or (maximum_altitude < 0.0):
            raise ValueError("ERROR in __init__ in Drone. Your Drone must have a valid maximum_altitude value.")
        if not isinstance(maximum_altitude, float):
            raise TypeError("ERROR in __init__ in Drone. Your Drone's maximum_altitude must be an instance of float.")
        if (maximum_weight is None) or (maximum_weight < 0.0):
            raise ValueError("ERROR in __init__ in Drone. Your Drone must have a valid maximum_weight value.")
        if not isinstance(maximum_weight, float):
            raise TypeError("ERROR in __init__ in Drone. Your Drone's maximum_weight must be an instance of float.")
        if (maximum_velocity is None) or (maximum_velocity < 0.0):
            raise ValueError("ERROR in __init__ in Drone. Your Drone must have a valid maximum_velocity value.")
        if not isinstance(maximum_velocity, float):
            raise TypeError("ERROR in __init__ in Drone. Your Drone's maximum_velocity must be an instance of float.")
        
        self.id = Drone._id_counter
        Drone._id_counter += 1

        self.altitude = 0.0
        self.maximum_altitude = maximum_altitude
        self.batery = 100.0
        self.current_position = None
        self.current_weight = 0.0
        self.maximum_weight = maximum_weight
        self.order = defaultdict(list)
        self.path = []
        self.velocity = 0.0
        self.maximum_velocity = maximum_velocity

    def add_new_order(self, client):
        """
        Adds a new order to Drone. An order is all Client's products at given moment. It is represented as a dictionary, 
        with Client as the Key and the products, its values. Whenever an order is taken, we should check if Client has made 
        an order before, if yes, we just add the new products.

        *IMPORTANT:* Must check if drone has available weight before getting the order

        Args:
            client (Client): Client that made the order.

        Raises:
            ValueError: If "client" has no products. 
            TypeError: If "client" is not an instance of Client.
        """

        # Sanity Check #
        if (not isinstance(client, Client)):
            raise TypeError("ERROR in add_new_order in Drone. Your client must be an instance of Client.")
        if ( len(client.products) == 0 ):
            raise ValueError("ERROR in add_new_order in Drone. Your client must have atleast one Product to make an order.")

        new_products = client.products
        if (client in self.order):
            current_order_client_items = self.order.get(client)
            new_products = list( set(client.products) - set(current_order_client_items) )
            

        for new_product in new_products:
            self.current_weight += new_product.weight
            self.order[client].append(new_product)

    def get_order(self, client):
        """
        Returns an Order of specified Client, if any found.

        Args:
            client (Client): Client to be found

        Returns:
            dict (dict{Client: list[Product]}): If order found, order with Key being Client instance and values, it's products. None, otherwise.

        Raises: 
            ValueError: If "client" is None (Invalid Client).
            TypeError: If "client" is not an instance of Client.
        """

        # Sanity Check. #
        if (client is None):
            raise ValueError("ERROR in get_order in Drone. Your client must be a real Client.")
        if (not isinstance(client, Client)):
            raise TypeError("ERROR in get_order in Drone. Your client must be an instance of Client.")
        
        order_dict = None
        if (client in self.order):
            current_order_client_items = self.order.get(client)
            order_dict = defaultdict(list)
            order_dict[client] = current_order_client_items
    
        return order_dict

    
    def get_drone_info(self):
        """
        Gets Drone's attributes.

        Returns:
            dict: Drone's attributes as a dictionary.
        """
        return self.__dict__