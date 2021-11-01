"""Main CLI Function
"""

import sys
import click
sys.path.append("/Users/joes/Desktop/Toy Robot Simulator")

from toy_robot_sim.app.constants import Constants
from toy_robot_sim.app.controller.move_controller import MoveController
from toy_robot_sim.app.controller.validation_controller import validate_move


def main() -> None:
    """Main execution funtion

    Returns:
        [tuple]: (x,y,Face)
    """
    commands = []
    place_command_seen = False
    while True:
        command = click.prompt("Please, place a move", type=str).upper()
        valid = validate_move(command)
        if valid == "place_command":
            place_command_seen = True
        if valid and place_command_seen:
            commands.append(command)
            if command.upper() == Constants.REPORT:
                response = MoveController(commands).calculate_move()
                print(response)
                return response


if __name__ == "__main__":
    main()
