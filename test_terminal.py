from unittest import TestCase
from tictactoe import terminal, X, O, EMPTY


# Define unit tests for terminal function
class TestTerminal(TestCase):
    def test_game_in_progress(self):
        self.assertFalse(
            terminal([
                [EMPTY, EMPTY, EMPTY],
                [EMPTY, EMPTY, EMPTY],
                [EMPTY, EMPTY, EMPTY]
            ])
        )
        self.assertFalse(
            terminal([
                [EMPTY, EMPTY, EMPTY],
                [EMPTY,   X  , EMPTY],
                [EMPTY, EMPTY, EMPTY]
            ])
        )
        self.assertFalse(
            terminal([
                [  O  , EMPTY, EMPTY],
                [EMPTY,   X  , EMPTY],
                [EMPTY, EMPTY, EMPTY]
            ])
        )

    def test_game_over(self):
        self.assertTrue(
            terminal([
                [  O  ,   X  , EMPTY],
                [EMPTY,   X  , EMPTY],
                [EMPTY,   X  ,   O  ]
            ])
        )
        self.assertTrue(
            terminal([
                [  O  , EMPTY, EMPTY],
                [  O  ,   X  ,   X  ],
                [  O  , EMPTY,   X  ]
            ])
        )
        self.assertTrue(
            terminal([
                [  X  ,   O  ,   O  ],
                [  O  ,   X  ,   X  ],
                [  X  ,   O  ,   X  ]
            ])
        )
