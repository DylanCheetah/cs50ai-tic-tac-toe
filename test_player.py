from unittest import TestCase
from tictactoe import player, X, O, EMPTY


# Define unit tests for player function
class TestPlayer(TestCase):
    def test_first_turn(self):
        self.assertEqual(
            player([
                [EMPTY, EMPTY, EMPTY],
                [EMPTY, EMPTY, EMPTY],
                [EMPTY, EMPTY, EMPTY]
            ]),
            X
        )

    def test_O_turn(self):
        self.assertEqual(
            player([
                [EMPTY, EMPTY, EMPTY],
                [EMPTY,   X  , EMPTY],
                [EMPTY, EMPTY, EMPTY]
            ]),
            O
        )

    def test_X_turn(self):
        self.assertEqual(
            player([
                [  O  , EMPTY, EMPTY],
                [EMPTY,   X  , EMPTY],
                [EMPTY, EMPTY, EMPTY]
            ]),
            X
        )
