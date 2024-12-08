from Product import Product
from Grid import Position
from Client import Client
from Order import Order

from collections import defaultdict

class Drone:
    """
    Drone class.

    Attributes:
        id                                       (int): Drone's IDentification number.
        altitude                               (float): Drone's current altitude.
        maximum_altitude                       (float): Drone's maximum altitude.
        battery                                (float): Drone's current battery.
        maximum_battery                        (float): Drone's maximum battery.
        current_position                    (Position): Drone's current grid Position (XYZ).
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
        self.battery = 5.0
        self.maximum_battery = 5.0
        self.current_position = None
        self.current_weight = 0.0
        self.maximum_weight = maximum_weight
        self.orders = defaultdict(list)
        self.path = []
        self.velocity = 0.0
        self.maximum_velocity = maximum_velocity

    def add_new_order(self, order):
        """
        Adds a new order to Drone.

        *IMPORTANT:* Must check if drone has available weight before getting the order

        Args:
            order (Order): Order that made the order.

        Raises:
            ValueError: If "order" has no products. 
            TypeError: If "order" is not an instance of Order.
        """

        # Sanity Check #
        if (not isinstance(order, Order)):
            raise TypeError("ERROR in add_new_order in Drone. Your order must be an instance of Order.")
        

        self.current_weight += order.total_weight
        for new_product in order.products:
            self.orders[order.client].append(new_product)
        
    def set_current_position(self, position):
        """
        Define drone's current position as Position. 

        Args:
            position (Position): Grid's position.

        """

        # Sanity Check #
        if (not isinstance(position, Position)):
            raise TypeError("ERROR in set_current_position in Drone. Your position must be an instance of Position.")
        
        self.current_position = position

    def get_order(self, client):
        """
        Returns an Order of specified Client, if any found.

        Args:
            client (Client): Client to be found

        Returns:
            dict (dict{Client: list[Product]}): If order found, order with Key being client and values it's products. None, otherwise.

        Raises: 
            ValueError: If "client" is None (Invalid Client).
            TypeError: If "client" is not an instance of Client.
        """

        # Sanity Check. #
        if (client is None):
            raise ValueError("ERROR in get_order in Drone. Your Order must have a valid client.")
        if (not isinstance(client, Client)):
            raise TypeError("ERROR in get_order in Drone. Your Client must be an instance of Client.")
        
        order_dict = None
        if (client in self.order):
            current_order_client_items = self.order.get(client)
            order_dict = defaultdict(list)
            order_dict[client] = current_order_client_items
    
        return order_dict
    
    def get_orders(self):
        """
        Return Drone's orders

        Returns:
            dict (dict{[Client]: list[Product]}): If drone has any order. None, otherwise.
        """

        return self.orders
    
    def clear_orders(self):
        """
        Clear drone's orders.
        """
        
        self.current_weight = 0.0
        self.orders.clear()

    def update_drone_velocity(self):
        """
        Returns drone's current velocity. It is defined by the function v = vmax * (1 - alpha * (weight/total_weight)) * (1 - beta * (height/total_height))

        Returns:
            velocity (float): Drone's currenty velocity.
        """
        alpha = 0.5
        beta = 0.2

        self.velocity = self.maximum_velocity * (1 - alpha * (self.current_weight / self.maximum_weight)) * (1 - beta * (self.altitude / self.maximum_altitude))
        return self.velocity

    def update_drone_battery(self, new_value):
        self.battery = new_value

    def get_drone_info(self):
        """
        Gets Drone's attributes.

        Returns:
            dict: Drone's attributes as a dictionary.
        """
        return self.__dict__