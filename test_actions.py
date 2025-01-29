from unittest import TestCase
from tictactoe import actions, X, O, EMPTY


# Define unit tests for the actions function
class TestActions(TestCase):
    def test_actions_available(self):
        # Generate correct actions list for a board with a single X in the center
        # and an O in the upper left
        correct_actions = set()

        for j in range(3):
            for i in range(3):
                if (i == 1 and j == 1) or (i == 0 and j == 0):
                    continue

                correct_actions.add((i, j))

        # Check the resulting actions
        self.assertEqual(
            actions([
                [  O  , EMPTY, EMPTY],
                [EMPTY,   X  , EMPTY],
                [EMPTY, EMPTY, EMPTY],
            ]),
            correct_actions
        )

    def test_actions_unavailable(self):
        self.assertEqual(
            actions([
                [  O  ,   X  ,   O  ],
                [  O  ,   X  ,   X  ],
                [  X  ,   O  ,   X  ],
            ]),
            set()
        )
