class Robot:
    def __init__(self, name):
        self.name = name
        self.direction = "NORTH"
        self.shield = None
        self.shots = None
        self.position = None
        self.status = "NORMAL"

    def set_initial_position(self, position):
        self.position = position

    def set_initial_shield(self, shield):
        self.shield = shield

    def set_initial_shots(self, shots):
        self.shots = shots

    def get_position(self):
        return self.position

    def get_shields(self):
        return self.shield

    def get_shots(self):
        return self.shots

    def get_position(self):
        return self.position

    def get_status(self):
        """Gets the robots status"""

        return self.status

    def get_direction(self):
        """Gets the current direction of the robot"""

        return self.direction

    def set_direction(self, direction):
        """Sets the new direction for the robot"""

        self.direction = direction
