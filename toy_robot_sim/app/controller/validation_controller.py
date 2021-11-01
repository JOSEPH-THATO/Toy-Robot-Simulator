""" Validation Controller
"""
import re
import sys
sys.path.append("/Users/joes/Desktop/Toy-Robot-Simulator")
from toy_robot_sim.app.constants import Constants


def validate_move(command):
    """Valide move to be taken

    Args:
        command (string): move command

    Returns:
        boolean/string:  True/False/place_command
    """
    if re.match(Constants.PLACE_REGEX, command):
        temp = command.split(" ")[1].split(",")
        x_co = int(temp[0])
        y_co = int(temp[1])
        face = temp[2].upper()

        if face not in Constants.FACE:
            return False

        if (
            x_co > Constants.MAX_X
            and y_co > Constants.MAX_Y
            or x_co > Constants.MAX_X
            or y_co > Constants.MAX_Y
        ):
            return False

        return "place_command"

    if command.upper() in [
        Constants.LEFT,
        Constants.RIGHT,
        Constants.MOVE,
        Constants.REPORT,
    ]:
        return True
    return False
