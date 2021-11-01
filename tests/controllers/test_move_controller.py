import sys
import unittest

sys.path.append("/Users/joes/Desktop/Toy Robot Simulator")
print(sys.path)

from toy_robot_sim.app.controller.move_controller import MoveController


class TestMoveController(unittest.TestCase):
    def test_calculate_move_with_valid_place(self):
        commands = ["PLACE 0,0,NORTH", "MOVE", "MOVE", "REPORT"]
        controller = MoveController(commands)
        x_co, y_co, face = controller.calculate_move()
        self.assertEqual(x_co, 0)
        self.assertEqual(y_co, 2)
        self.assertEqual(face, "NORTH")

    def test_calculate_move_with_valid_north_turn(self):
        commands = ["PLACE 2,0,NORTH", "LEFT", "MOVE", "REPORT"]
        controller = MoveController(commands)
        x_co, y_co, face = controller.calculate_move()
        self.assertEqual(x_co, 1)
        self.assertEqual(y_co, 0)
        self.assertEqual(face, "WEST")

    def test_calculate_move_with_valid_south_turn(self):
        commands = [
            "PLACE 2,1,SOUTH",
            "RIGHT",
            "MOVE",
            "LEFT",
            "MOVE",
            "REPORT"
        ]
        controller = MoveController(commands)
        x_co, y_co, face = controller.calculate_move()
        self.assertEqual(x_co, 3)
        self.assertEqual(y_co, 2)
        self.assertEqual(face, "NORTH")

    def test_calculate_move_with_valid_east_turn(self):
        commands = [
            "PLACE 0,0,EAST",
            "LEFT",
            "MOVE",
            "RIGHT",
            "MOVE",
            "RIGHT",
            "REPORT",
        ]
        controller = MoveController(commands)
        x_co, y_co, face = controller.calculate_move()
        self.assertEqual(x_co, 1)
        self.assertEqual(y_co, 1)
        self.assertEqual(face, "SOUTH")

    def test_calculate_move_with_valid_west_turn(self):
        commands = [
            "PLACE 2,2,WEST",
            "LEFT",
            "MOVE",
            "LEFT",
            "MOVE",
            "RIGHT",
            "REPORT"
        ]
        controller = MoveController(commands)
        x_co, y_co, face = controller.calculate_move()
        self.assertEqual(x_co, 1)
        self.assertEqual(y_co, 1)
        self.assertEqual(face, "NORTH")
