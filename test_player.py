import unittest
from player import Player, ComputerPlayer, SuperComputerPlayer


class TestPlayer(unittest.TestCase):

    def test_player(self):
        with self.subTest('has name'):
            player = Player("1", "x")
            expected_output = "1"
            result = player.get_name()
            self.assertEqual(result, expected_output)

        with self.subTest('has mark'):
            player = Player("2", "o")
            expected_output = "o"
            result = player.get_mark()
            self.assertEqual(result, expected_output)


class TestComputerPlayer(unittest.TestCase):
    def setUp(self):
        self.player = ComputerPlayer("1", "x")

    def test_computer_player(self):
        with self.subTest('has name'):
            expected_output = "1"
            result = self.player.get_name()
            self.assertEqual(result, expected_output)

        with self.subTest('has mark'):
            expected_output = "x"
            result = self.player.get_mark()
            self.assertEqual(result, expected_output)

    def test_make_move(self):
        test_cases = [
            {
                "name": "no moves played",
                "board": [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                "expected_output": 1
            },
            {
                "name": "one move played",
                "board": [["x", 2, 3], [4, 5, 6], [7, 8, 9]],
                "expected_output": 2
            },
            {
                "name": "two moves played",
                "board": [["x", "o", 3], [4, 5, 6], [7, 8, 9]],
                "expected_output": 3
            },
            {
                "name": "multiple out of order moves played",
                "board": [["x", 2, "o"], ["o", 5, "x"], [7, "x", 9]],
                "expected_output": 2
            },
            {
                "name": "multiple out of order moves played",
                "board": [["x", "x", "o"], ["o", 5, "x"], [7, "x", 9]],
                "expected_output": 5
            },
            {
                "name": "all but one moves played",
                "board": [["x", "o", "x"], ["x", "o", "x"], ["o", "x", 9]],
                "expected_output": 9
            }
        ]

        for test_case in test_cases:
            with self.subTest(test_case["name"]):
                board = test_case["board"]
                expected_output = test_case["expected_output"]

                result = self.player.make_move(board)

                self.assertEqual(result, expected_output)


class TestSuperComputerPlayer(unittest.TestCase):
    def setUp(self):
        self.player = SuperComputerPlayer("Super Bot", "x")

    def test_computer_player(self):
        with self.subTest('has name'):
            expected_output = "Super Bot"
            result = self.player.get_name()
            self.assertEqual(result, expected_output)

        with self.subTest('has mark'):
            expected_output = "x"
            result = self.player.get_mark()
            self.assertEqual(result, expected_output)

    def test_make_move(self):
        test_cases = [{'name': "ai should take middle cell on first move",
                       'board': [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                       'expected_move': 5},
                      {'name': "ai should take winning diagonal move",
                       'board': [["x", "o", "x"], [4, 5, "o"], ["x", "o",  9]],
                       'expected_move': 4},
                      {'name': "ai should take winning horizontal move",
                       'board': [["x", "x", 3], [4, 5, "o"], [7, "o", 9]],
                       'expected_move': 3},
                      {'name': "ai should take winning vertical move",
                       'board': [["x", 2, 3], [4, 5, "o"], ["x", "o", 9]],
                       'expected_move': 4},
                      {'name': "ai should block opponent's two-move win",
                       'board': [['x', 2, 3], [4, 'o', 6], [7, 8, 'x']],
                       'expected_move': 3},
                      {'name': "ai should block opponent's diagonal win",
                       'board': [["o", "x", 3], [4, 5, "x"], [7, 8, "o"]],
                       'expected_move': 5},
                      {'name': "ai should block opponent's vertical win",
                       'board': [["o", "x", 3], ["o", 5, "x"], [7, 8, 9]],
                       'expected_move': 7},
                      {'name': "ai should block opponent's horizontal win",
                       'board': [["x", "o", "x"], ["o", 5, "o"], [7, 8, "x"]],
                       'expected_move': 5},
                      {'name': "ai should choose the last move available if all but one move is left",
                       'board': [["o", "x", "o"], ["x", "o", "x"], ["x", "o", 9]],
                       'expected_move': 9}
                      ]

        for test_case in test_cases:
            with self.subTest(test_case['name']):
                expected_move = test_case['expected_move']
                result = self.player.make_move(test_case['board'])
                self.assertEqual(expected_move, result)

    def test_is_no_moves_made(self):
        test_cases = [
            {
                'name': "should return true when no one has made a move yet",
                'board': [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                'expected_result': True
            },
            {
                'name': "should return false when at least one person has made a move",
                'board': [[1, 2, 3], [4, 'x', 6], [7, 8, 9]],
                'expected_result': False
            }
        ]

        for test_case in test_cases:
            with self.subTest(test_case['name']):
                board = test_case['board']
                expected_result = test_case['expected_result']
                self.assertEqual(self.player.is_no_moves_made(board), expected_result)

    def test_is_moves_left(self):
        test_cases = [
            {
                'name': "should return false when no moves left",
                'board': [['x', 'o', 'x'], ['x', 'o', 'x'], ['o', 'x', 'o']],
                'expected_result': False
            },
            {
                'name': "should return true when one move left",
                'board': [['x', 'o', 'x'], ['x', 'o', 'x'], ['o', 8, 'o']],
                'expected_result': True
            },
            {
                'name': "should return true when multiple moves left",
                'board': [['x', 'o', 'x'], ['x', 5, 'x'], ['o', 8, 'o']],
                'expected_result': True
            }
        ]

        for test_case in test_cases:
            with self.subTest(test_case['name']):
                board = test_case['board']
                expected_result = test_case['expected_result']
                self.assertEqual(self.player.is_moves_left(board), expected_result)

    def test_evaluate(self):
        test_cases = [{'name': "should return 10 if computer wins",
                       'board': [['x', 'x', 'x'], ['o', 'x', 'x'], ['x', 8, 9]],
                       'expected_result': 10},
                      {'name': "should return -10 if opponent wins",
                       'board': [['o', 'x', 'x'], ['o', 'o', 'o'], [7, 'x', 9]],
                       'expected_result': -10},
                      {'name': "should return 0 if it is a draw",
                       'board': [['o', 'x', 'o'], ['x', 'x', 'o'], ['o', 'o', 'x']],
                       'expected_result': 0}]

        for test_case in test_cases:
            with self.subTest(test_case['name']):
                expected_result = test_case['expected_result']
                result = self.player.evaluate(test_case['board'])
                self.assertEqual(result, expected_result)

    def test_minimax(self):
        test_cases = [
            {'name': "should return the highest position score if maximizer won",
             'board': [[1, 'o', 'x'], ['o', 'x', 6], ['x', 8, 'o']],
             'depth': 0,
             'is_max': True,
             'expected_result': 10},
            {'name': "should return the lowest position score if minimizer won",
             'board': [[1, 'o', 'x'], ['x', 'o', 6], [7, 'o', 'o']],
             'depth': 0,
             'is_max': False,
             'expected_result': -10},
            {'name': "should return a high position score if maximizer can win in one move",
             'board': [[1, 'o', 'x'], ['o', 'x', 6], [7, 8, 'o']],
             'depth': 0,
             'is_max': True,
             'expected_result': 9},
            {'name': "should return a low position score if minimizer can win in one move",
             'board': [[1, 'o', 'x'], ['x', 'o', 6], [7, 8, 'o']],
             'depth': 0,
             'is_max': False,
             'expected_result': -9},
            {'name': "should return a high position score if maximizer can block minimizer's two-move win",
             'board': [['x', 2, 3], [4, 'o', 6], [7, 'x', 9]],
             'depth': 0,
             'is_max': True,
             'expected_result': 7},
            {'name': "should return a low position score if minimizer can block maximizer's two-move win",
             'board': [[1, 2, 'o'], ['x', 5, 6], [7, 'o', 'x']],
             'depth': 0,
             'is_max': False,
             'expected_result': -7},
            {'name': "should return a highish position score if maximizer can win in three moves",
             'board': [['x', 'o', 'x'], [4, 5, 6], [7, 'x', 'o']],
             'depth': 0,
             'is_max': True,
             'expected_result': 7},
            {'name': "should return a lowish position score if minimizer can win in three moves",
             'board': [[1, 2, 'o'], [4, 5, 6], ['x', 'x', 'o']],
             'depth': 0,
             'is_max': True,
             'expected_result': -6}
        ]

        for test_case in test_cases:
            with self.subTest(test_case['name']):
                result = self.player.minimax(test_case['board'],
                                             test_case['depth'],
                                             test_case['is_max'])
                expected_result = test_case['expected_result']
                self.assertEqual(result, expected_result)
