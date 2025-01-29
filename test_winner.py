from unittest import TestCase
from tictactoe import winner, X, O, EMPTY


# Define unit tests for winner function
class TestWinner(TestCase):
    def test_X_wins(self):
        self.assertEqual(
            winner([
                [  O  , EMPTY, EMPTY],
                [  X  ,   X  ,   X  ],
                [EMPTY,   O  , EMPTY]
            ]),
            X
        )
        self.assertEqual(
            winner([
                [  O  , EMPTY, EMPTY],
                [EMPTY,   O  , EMPTY],
                [  X  ,   X  ,   X  ]
            ]),
            X
        )
        self.assertEqual(
            winner([
                [  X  ,   X  ,   X  ],
                [  O  , EMPTY, EMPTY],
                [EMPTY,   O  , EMPTY]
            ]),
            X
        )
        self.assertEqual(
            winner([
                [  O  ,   X  ,   O  ],
                [  X  ,   X  ,   O  ],
                [EMPTY,   X  , EMPTY]
            ]),
            X
        )
        self.assertEqual(
            winner([
                [  O  , EMPTY,   X  ],
                [EMPTY,   X  , EMPTY],
                [  X  , EMPTY,   O  ]
            ]),
            X
        )

    def test_O_wins(self):
        self.assertEqual(
            winner([
                [  O  ,   O  ,   O  ],
                [  X  ,   X  ,   O  ],
                [  X  , EMPTY,   X  ]
            ]),
            O
        )
        self.assertEqual(
            winner([
                [  O  ,   X  , EMPTY],
                [EMPTY,   O  , EMPTY],
                [  X  ,   X  ,   O  ]
            ]),
            O
        )

    def test_no_winner(self):
        self.assertEqual(
            winner([
                [EMPTY, EMPTY, EMPTY],
                [EMPTY, EMPTY, EMPTY],
                [EMPTY, EMPTY, EMPTY]
            ]),
            None
        )
        self.assertEqual(
            winner([
                [  O  ,   X  ,   O  ],
                [  O  ,   X  ,   X  ],
                [  X  ,   O  ,   X  ]
            ]),
            None
        )
