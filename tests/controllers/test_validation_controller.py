import sys
import unittest

sys.path.append("/Users/joes/Desktop/Toy-Robot-Simulator")
print(sys.path)

from toy_robot_sim.app.controller.validation_controller import validate_move


class TestValidationController(unittest.TestCase):
    def test_validate_move_with_valid_place_command(self):
        move = "PLACE 0,0,NORTH"
        res = validate_move(move)
        self.assertEqual(res, "place_command")

    def test_validate_move_with_invalid_x_y_place_command(self):
        move = "PLACE 6,6,NORTH"
        res = validate_move(move)
        self.assertEqual(res, False)

    def test_validate_move_with_valid_move_command(self):
        move = "MOVE"
        res = validate_move(move)
        self.assertEqual(res, True)

    def test_validate_move_with_invalid_move_command(self):
        move = "TEST"
        res = validate_move(move)
        self.assertEqual(res, False)

    def test_validate_move_with_invalid_face_place_command(self):
        moves = "PLACE 0,0,TEST"
        res = validate_move(moves)
        self.assertEqual(res, False)
