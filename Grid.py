class Grid:
    """
    Grid class.

    Attributes: 
        height               (int): Grid's height.
        width                (int): Grid's width.
        positions (list[Position]): Possible positions in Grid.
    """

    def __init__(self, height, width):
        """
        Initiates a new Grid instance with specified values. Null or invalid values are considered as an error (raises ValueError or TypeError).

        Args:
            height (int): Grid's height.
            width  (int): Grid's width.

        Raises:
            ValueError: If attributes "height", "width" are either None or invalid (Negative values).
            TypeError: If attributes "height", "width" have incorrect types.
    
        """

        # Sanity Check #
        if (height is None) or (height < 0):
            raise ValueError("ERROR in __init__ in Grid. Your Grid must have a valid height.")
        if not isinstance(height, int):
            raise TypeError("ERROR in __init__ in Grid. Your Grid's height must be an instance of int.")
    
        if (width is None) or (width < 0):
            raise ValueError("ERROR in __init__ in Grid. Your Grid must have a valid width.")
        if not isinstance(width, int):
            raise TypeError("ERROR in __init__ in Grid. Your Grid's width must be an instance of int.")

        self.height = height
        self.width = width
        self.positions = []

        # Read file with altitude values ​​at each grid position
        with open('./archives/altitude1.txt', 'r') as arquivo:
            lines = arquivo.readlines()

        for x in range(0, self.height):
            for y in range(0, self.width):
                z = int (lines[(x * self.width) + y].strip())
                self.positions.append(Position(x, y, z))

    def check_position_in_grid(self, position):
        """
        Checks if a specified "position" is in between Grid's limits.

        Args:
            position (Position): Desired "position" to be checked.
            
        Returns:
            bool: True if "position" between Grid's limits. False otherwise.        

        Raises:
            TypeError: If "position" is not an instance of Product.
        """

        # Sanity Check #
        if not isinstance(position, Position):
            raise TypeError("ERROR in check_position_in_grid in Grid. Only Position instances can be checked.")

        #                                Validating X                                                    Validating Y
        is_valid = ( (( position.X >= 0 ) and ( position.X < self.width )) and (( position.Y >= 0 ) and ( position.Y < self.height )) )

        return is_valid


    def get_position_in_grid(self, X, Y):
        """
        Gets Grid's Position with specified XY.

        Args: 
            X (int): Position's X value.
            Y (int): Position's Y value.
        
        Returns:
            Position: Returns a Grid Position if exists. None otherwise.

        Raises:
            ValueError: If attributes "X", "Y" are None.
            TypeError: If attributes "X", "Y" have incorrect types.
        """

        # Sanity Check #
        if (X is None):
            raise ValueError("ERROR in get_position_in_grid in Grid. Your Position must have a valid X value.")
        if (not isinstance(X, int)):
            raise TypeError("ERROR in get_position_in_grid in Grid. Your Position's X must be an instance of int.")

        if (Y is None):
            raise ValueError("ERROR in get_position_in_grid in Grid. Your Position must have a valid Y value.")
        if (not isinstance(Y, int)):
            raise TypeError("ERROR in get_position_in_grid in Grid. Your Position's Y must be an instance of int.")
        

        return_position = None
        if ( self.check_position_in_grid(Position(X,Y, 0)) ):
            return_position = self.positions[(X * self.width) + Y]

        return return_position
    
    def get_neighbors(self, position):
        """
        Returns "position"'s neighbors (neighborhood of 8) positions as a list.

        Args:
            position (Position): Desired "position" to get neighbors

        Returns:
            neighbors (list[Position]): Grid's "position"'s neighbors
        """

        # Sanity Check #
        if not isinstance(position, Position):
            raise TypeError("ERROR in check_position_in_grid in Grid. Only Position instances can be checked.")

        neighbors = []
        position_x = position.X
        position_y = position.Y

        ## X-1 Y-1
        position_neighbor = self.get_position_in_grid((position_x - 1), position_y - 1)
        if position_neighbor != None: neighbors.append(position_neighbor)

        ## X-1 Y
        position_neighbor = self.get_position_in_grid((position_x - 1), position_y)
        if position_neighbor != None: neighbors.append(position_neighbor)

        ## X-1 Y+1
        position_neighbor = self.get_position_in_grid((position_x - 1), position_y + 1)
        if position_neighbor != None: neighbors.append(position_neighbor)

        ## X   Y-1
        position_neighbor = self.get_position_in_grid((position_x), position_y - 1)
        if position_neighbor != None: neighbors.append(position_neighbor)

        ## X   Y+1
        position_neighbor = self.get_position_in_grid((position_x), position_y + 1)
        if position_neighbor != None: neighbors.append(position_neighbor)

        ## X+1 Y-1
        position_neighbor = self.get_position_in_grid((position_x + 1), position_y - 1)
        if position_neighbor != None: neighbors.append(position_neighbor)

        ## X+1 Y
        position_neighbor = self.get_position_in_grid((position_x + 1), position_y)
        if position_neighbor != None: neighbors.append(position_neighbor)

        ## X+1 Y+1
        position_neighbor = self.get_position_in_grid((position_x + 1), position_y + 1)
        if position_neighbor != None: neighbors.append(position_neighbor)

        return neighbors

    def grid_update_position_classification(self):
        for position in self.positions:
            if position.classification == "drone":
                position.set_position_classification(position.last_classification)

    def get_grid_info(self):
        """
        Gets Grids's attributes.

        Returns: 
            dict: Grids's attributes as a dictionary.
        """
        return self.__dict__

    def __str__(self):
        """
        Returns stringfied representation of a Grid instance.

        Returns:
            str: Stringfied representation of a Grid instance.
        """

        # return_string = ""

        # for i in range(0, self.height):
        #     return_string += "|"
        #     for j in range(0, self.width):
        #         return_string += f"{str(self.positions[(i * self.width) +  j])}|"

        #     return_string += "\n"
        # return return_string

        return_string = "   "  # Espaço inicial para alinhar com os índices das linhas

        # Adicionar cabeçalho com os índices das colunas
        for j in range(self.width):
            return_string += f"{j:>2} "  # Formata os índices das colunas com largura fixa
        return_string += "\n"

        # Construir as linhas da grid
        for i in range(self.height):
            return_string += f"{i:>2}|"  # Adiciona o índice da linha no início
            for j in range(self.width):
                value = str(self.positions[(i * self.width) + j])  # Obtém o valor na posição
                return_string += f"{value:>2}|"  # Adiciona o valor com largura fixa
            return_string += "\n"

        return return_string

class Position:
    """
    Position class.

    Attributes:
        X                       (int): Position's X value.
        Y                       (int): Position's Y value.
        Z                       (int): Altitude of point (X, Y).
        current_classification  (str): Position's classification. Can be "client", "base", "drone" or "none"
        last_classification     (str): Position's last classification. Can be "client", "base", "drone" or "none"
    """

    def __init__(self, X, Y, Z):
        """
        Initiates a new Position instance with specified values. Null or invalid values are considered as an error (raises ValueError TypeError).

        Args: 
            X (int): X value, related to GRID.
            Y (int): Y value, related to GRID.
            Z (int): Z value, related to GRID.

        Raises:
            ValueError: If attributes "X", "Y", "Z"  are None.
            TypeError: If attributes "X", "Y", "Z" have incorrect types.
        """

        # Sanity Check #
        if (X is None):
            raise ValueError("ERROR in __init__ in Position. Your Position must have a valid X value.")
        if (not isinstance(X, int)):
            raise TypeError("ERROR in __init__ in Position. Your Position's X must be an instance of int.")

        if (Y is None):
            raise ValueError("ERROR in __init__ in Position. Your Position must have a valid Y value.")
        if (not isinstance(Y, int)):
            raise TypeError("ERROR in __init__ in Position. Your Position's Y must be an instance of int.")

        if (Z is None):
            raise ValueError("ERROR in __init__ in Position. Your Position must have a valid Z value.")
        if (not isinstance(Z, int)):
            raise TypeError("ERROR in __init__ in Position. Your Position's Z must be an instance of int.")
        
        self.X = X
        self.Y = Y
        self.Z = Z
        self.classification = "none"
        self.last_classification = "none"

    def set_position_classification(self, classification):
        """
        Sets position's classifcation with "classification". It can be "client", "base", "drone" or "none".

        Args:
            classification (str): Classification
        
        Raises: 
            ValueError: If arg "classification" is empty string or None.
            TypeError: if arg "classification" type is different than "str".
        """
        if (classification != "client" and classification != "base" and classification != "drone" and classification != "none") or (classification is None):
            raise ValueError("ERROR in __init__ in Position. Your Position must have a valid classification ('client', 'base' or 'none').")
        if (not isinstance(classification, str)):
            raise TypeError("ERROR in __init__ in Position. Your Position's classification must be an instance of str.")
        
        self.last_classification = self.classification
        self.classification = classification

    def get_position_info(self):
        """
        Gets Position's attributes.

        Returns: 
            dict: Position's attributes as a dictionary.
        """

        return self.__dict__

    def __str__(self):
        """
        Returns stringfied representation of a Position instance.

        Returns:
            str: Stringfied representation of a Position instance.
        """

        return_string = ""
        if (self.classification == "base"): return_string = "B"
        elif (self.classification == "client"): return_string = "C"
        elif (self.classification == "drone"): return_string = "D"
        elif   (self.classification == "none" ): return_string = "-"

        return return_string
    