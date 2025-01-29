from unittest import TestCase
from tictactoe import utility, X, O, EMPTY


# Define unit tests for utility function
class TestUtility(TestCase):
    def test_X_wins(self):
        self.assertEqual(
            utility([
                [  O  ,   X  ,   O  ],
                [EMPTY,   X  , EMPTY],
                [EMPTY,   X  , EMPTY]
            ]),
            1
        )

    def test_O_wins(self):
        self.assertEqual(
            utility([
                [  O  , EMPTY, EMPTY],
                [  O  ,   X  ,   X  ],
                [  O  , EMPTY,   X  ]
            ]),
            -1
        )

    def test_tie(self):
        self.assertEqual(
            utility([
                [  O  ,   X  ,   O  ],
                [  O  ,   X  ,   X  ],
                [  X  ,   O  ,   X  ]
            ]),
            0
        )
