from unittest import TestCase
from tictactoe import result, X, O, EMPTY


# Define unit tests for result function
class TestResult(TestCase):
    def test_X_move(self):
        self.assertEqual(
            result(
                [
                    [EMPTY, EMPTY, EMPTY],
                    [EMPTY, EMPTY, EMPTY],
                    [EMPTY, EMPTY, EMPTY]
                ],
                (1, 1)
            ),
            [
                [EMPTY, EMPTY, EMPTY],
                [EMPTY,   X  , EMPTY],
                [EMPTY, EMPTY, EMPTY]
            ]
        )

    def test_O_move(self):
        self.assertEqual(
            result(
                [
                    [EMPTY, EMPTY, EMPTY],
                    [EMPTY,   X  , EMPTY],
                    [EMPTY, EMPTY, EMPTY]
                ],
                (0, 0)
            ),
            [
                [  O  , EMPTY, EMPTY],
                [EMPTY,   X  , EMPTY],
                [EMPTY, EMPTY, EMPTY]
            ]
        )

    def test_invalid_move(self):
        self.assertRaises(
            Exception,
            result,
            [
                [  O  , EMPTY, EMPTY],
                [EMPTY,   X  , EMPTY],
                [EMPTY, EMPTY, EMPTY]
            ],
            (0, 0)
        )
