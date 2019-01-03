"""
    Unit Tests for Sudoku
"""
import sudoku
import unittest


class TestSudoku(unittest.TestCase):
    def test_solved(self):
        """
            Test that a solved puzzle will be marked solved
        """
        # solved sudoku puzzle
        grid = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
                [7, 8, 9, 1, 2, 3, 4, 5, 6],
                [4, 5, 6, 7, 8, 9, 1, 2, 3],
                [3, 1, 2, 8, 4, 5, 9, 6, 7],
                [6, 9, 7, 3, 1, 2, 8, 4, 5],
                [8, 4, 5, 6, 9, 7, 3, 1, 2],
                [2, 3, 1, 5, 7, 4, 6, 9, 8],
                [9, 6, 8, 2, 3, 1, 5, 7, 4],
                [5, 7, 4, 9, 6, 8, 2, 3, 1]]

        self.assertTrue(sudoku.is_solved(grid))

    def test_column_not_solved(self):
        """
            Test that columns with the same values will not be solved
        """
        grid = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9]]

        self.assertFalse(sudoku.is_solved(grid))

    def test_row_not_solved(self):
        """
            Test that rows with the same values will not be solved
        """
        grid = [[1, 1, 1, 1, 1, 1, 1, 1, 1],
                [2, 2, 2, 2, 2, 2, 2, 2, 2],
                [3, 3, 3, 3, 3, 3, 3, 3, 3],
                [4, 4, 4, 4, 4, 4, 4, 4, 4],
                [5, 5, 5, 5, 5, 5, 5, 5, 5],
                [6, 6, 6, 6, 6, 6, 6, 6, 6],
                [7, 7, 7, 7, 7, 7, 7, 7, 7],
                [8, 8, 8, 8, 8, 8, 8, 8, 8],
                [9, 9, 9, 9, 9, 9, 9, 9, 9]]
        self.assertFalse(sudoku.is_solved(grid))

    def test_incomplete_solution(self):
        """
            Test that an incomplete solution will be marked unsolved
        """
        grid = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
                [7, 8, 9, 1, 2, 3, 4, 5, None],
                [4, 5, 6, 7, 8, 9, 1, 2, 3],
                [3, 1, 2, 8, 4, 5, 9, 6, 7],
                [6, 9, 7, 3, 1, 2, 8, 4, 5],
                [8, 4, 5, 6, 9, 7, 3, 1, 2],
                [2, 3, 1, 5, 7, 4, 6, 9, 8],
                [9, 6, 8, 2, 3, 1, 5, 7, 4],
                [None, 7, 4, 9, 6, 8, 2, 3, 1]]

        self.assertFalse(sudoku.is_solved(grid))

    def test_csp_search(self):
        grid = [[None, 2, 3, 4, 5, 6, 7, 8, 9],
                [7,    8, 9, 1, 2, 3, 4, 5, 6],
                [4,    5, 6, 7, 8, 9, 1, 2, 3],
                [3,    1, 2, 8, 4, 5, 9, 6, 7],
                [6,    9, 7, 3, 1, 2, 8, 4, 5],
                [8,    4, 5, 6, 9, 7, 3, 1, 2],
                [2,    3, 1, 5, 7, 4, 6, 9, 8],
                [9,    6, 8, 2, 3, 1, 5, 7, 4],
                [5,    7, 4, 9, 6, 8, 2, 3, 1]]
        expected_values = {(0, 0, 1)}
        for assignment in sudoku.csp_search(grid):
            self.assertTrue(assignment in expected_values)
            expected_values.remove(assignment)

    def test_csp_search2(self):
        grid = [[None, 2, 3, 4,    5, 6, 7, 8, 9],
                [7,    8, 9, 1,    2, 3, 4, 5, 6],
                [4,    5, 6, 7,    8, 9, 1, 2, 3],
                [3,    1, 2, 8,    4, 5, 9, 6, 7],
                [6,    9, 7, None, 1, 2, 8, 4, 5],
                [8,    4, 5, 6,    9, 7, 3, 1, 2],
                [2,    3, 1, 5,    7, 4, 6, 9, 8],
                [9,    6, 8, 2,    3, 1, 5, 7, 4],
                [5,    7, 4, 9,    6, 8, 2, 3, None]]
        expected_values = {(0, 0, 1), (8, 8, 1), (4, 3, 3)}
        for assignment in sudoku.csp_search(grid):
            self.assertTrue(assignment in expected_values)
            expected_values.remove(assignment)

    def test_csp_search3(self):
        grid = [[None, None, None, None, None, None, None, 6,    None],
                [None, None, 1,    None, None, None, None, None, None],
                [None, None, None, None, None, None, None, 6,    None],
                [None, None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None],
                [6,    None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None]]
        expected_values = {(1, 1, 6)}
        assignment = next(sudoku.csp_search(grid))
        self.assertTrue(assignment in expected_values)

    def test_bad_csp_search(self):
        grid = [[None, None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None]]
        # Python generators raise a StopIteration exception when they return.
        self.assertRaises(StopIteration, next, sudoku.csp_search(grid))

    def test_easy_solve(self):
        # This is an "easy" sudoku problem pulled from the internet
        grid = [[None, None, 3, None, 7, 4, None, 1, None],
                [8, None, None, 5, 6, 9, None, 4, None],
                [6, None, None, None, 2, 1, None, None, 8],
                [None, 1, None, None, 4, 7, 9, None, None],
                [2, None, None, None, None, None, None, None, 3],
                [None, None, 4, 2, 3, None, None, 6, None],
                [1, None, None, 7, 9, None, None, None, 4],
                [None, 7, None, 4, 8, 6, None, None, 2],
                [None, 3, None, 1, 5, None, 7, None, None]]
        solved_grid = sudoku.solve(grid)
        self.assertTrue(sudoku.is_solved(solved_grid),
                        "\n" + sudoku.grid_str(solved_grid))

    @unittest.skip("Not ready for this one yet")
    def test_hard_solve(self):
        grid = [[None, None, None, None, 6,    None, None, None, 3],
                [None, None, None, None, None, None, None, 4,    2],
                [None, None, 3,    9,    2,    None, 7,    None, None],
                [4,    None, None, 3,    None, None, None, 7,    None],
                [None, None, 6,    None, None, None, 8,    None, None],
                [None, 2,    None, None, None, 7,    None, None, 9],
                [None, None, 9,    None, 5,    2,    3,    None, None],
                [6,    8,    None, None, None, None, None, None, None],
                [7,    None, None, None, 1,    None, None, None, None]]
        # solution = [[2, 5, 4, 7, 6, 1, 9, 8, 3],
        #             [9, 6, 7, 5, 3, 8, 1, 4, 2],
        #             [8, 1, 3, 9, 2, 4, 7, 5, 6],
        #             [4, 9, 1, 3, 8, 6, 2, 7, 5],
        #             [3, 7, 6, 2, 9, 5, 8, 1, 4],
        #             [5, 2, 8, 1, 4, 7, 6, 3, 9],
        #             [1, 4, 9, 8, 5, 2, 3, 6, 7],
        #             [6, 8, 2, 4, 7, 3, 5, 9, 1],
        #             [7, 3, 5, 6, 1, 9, 4, 2, 8]]
        solved_grid = sudoku.solve(grid)
        print(sudoku.grid_str(solved_grid))
        self.assertTrue(sudoku.is_solved(solved_grid),
                        "\n" + sudoku.grid_str(solved_grid))
