from unittest import TestCase
from tictactoe import minimax, X, O, EMPTY


# Define unit tests for minimax function
class TestMinimax(TestCase):
    def test_first_move(self):
        self.assertEqual(
            minimax([
                [EMPTY, EMPTY, EMPTY],
                [EMPTY, EMPTY, EMPTY],
                [EMPTY, EMPTY, EMPTY]
            ]),
            (0, 1)
        )

    def test_second_move(self):
        self.assertEqual(
            minimax([
                [  X  , EMPTY, EMPTY],
                [EMPTY, EMPTY, EMPTY],
                [EMPTY, EMPTY, EMPTY]
            ]),
            (1, 1)
        )
