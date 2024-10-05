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

        for x in range(0, self.height):
            for y in range(0, self.width):
                self.positions.append(Position(x, y))

        
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
        if ( self.check_position_in_grid(Position(X,Y)) ):
            return_position = self.positions[(X * self.width) + Y]

        return return_position


    def get_grid(self):
        """
        Gets Grids's attributes.

        Returns: 
            dict: Grids's attributes as a dictionary.
        """
        return self.__dict__



class Position:
    """
    Position class.

    Attributes:
        X (int): Position's X value.
        Y (int): Position's Y value.
    """

    def __init__(self, X, Y):
        """
        Initiates a new Position instance with specified values. Null or invalid values are considered as an error (raises ValueError TypeError).

        Args: 
            X (int): X value, related to GRID.
            Y (int): Y value, related to GRID.

        Raises:
            ValueError: If attributes "X", "Y" are None.
            TypeError: If attributes "X", "Y" have incorrect types.
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
        
        self.X = X
        self.Y = Y

    def get_position(self):
        """
        Gets Position's attributes.

        Returns: 
            dict: Position's attributes as a dictionary.
        """

        return self.__dict__
    