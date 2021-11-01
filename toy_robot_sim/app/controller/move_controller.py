"""Move Controller
"""

from toy_robot_sim.app.constants import Constants


class MoveController:
    def __init__(self, commands: list):
        self.commands = commands
        self.x_co = 0
        self.y_co = 0
        self.direction = ""

    def calculate_move(self):
        """Calculate robot move
        """
        if self.commands:
            for command in self.commands:
                if "PLACE" in command:
                    self._get_position(command)

                if command == Constants.MOVE:
                    self._make_a_move()

                if command in [Constants.LEFT, Constants.RIGHT]:
                    self._rotate_robot(command)

                if command == Constants.REPORT:
                    return self.x_co, self.y_co, self.direction
        return None

    def _get_position(self, command):
        """Get the possion from PLACE command
        """
        position = command.split(" ")[1].split(",")
        self.x_co = int(position[0])
        self.y_co = int(position[1])
        self.direction = position[2]

    def _make_a_move(self):
        """Move the robot
        """
        if self.direction == "NORTH":
            if self.y_co + 1 <= 5:
                self.y_co += 1
        elif self.direction == "SOUTH":
            if self.y_co - 1 >= 0:
                self.y_co -= 1
        elif self.direction == "EAST":
            if self.x_co + 1 <= 5:
                self.x_co += 1
        elif self.direction == "WEST":
            if self.x_co - 1 >= 0:
                self.x_co -= 1

    def _rotate_robot(self, command):
        """Rotate the robot by 90 degrees
        """
        if command == Constants.LEFT:
            if self.direction == "NORTH":
                self.direction = "WEST"
            elif self.direction == "SOUTH":
                self.direction = "WEST"
            elif self.direction == "EAST":
                self.direction = "NORTH"
            elif self.direction == "WEST":
                self.direction = "SOUTH"

        if command == Constants.RIGHT:
            if self.direction == "NORTH":
                self.direction = "EAST"
            elif self.direction == "SOUTH":
                self.direction = "EAST"
            elif self.direction == "EAST":
                self.direction = "SOUTH"
            elif self.direction == "WEST":
                self.direction = "NORTH"
