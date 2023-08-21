class Position:

    def __init__(self, coordinates):
        self.x_coordinate = coordinates[0]
        self.y_coordinate = coordinates[1]

    def __eq__(self, other):
        x_bool = self.x_coordinate == other.x_coordinate
        y_bool = self.y_coordinate == other.y_coordinate
        return x_bool and y_bool
